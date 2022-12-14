from flask import Flask, request
import pyotp

import extensions.caesar
import extensions.rsa
import extensions.crud

app = Flask(__name__)

key_value_dict = {}
users = {"admin" : "hello123"}

# roles: user, admin
current_role = 'guest'

# access with user 
def caesar1(message, mode):
  global current_role
  # Caesar 1
  if current_role == "user" or current_role == "admin":
    if mode == "encrypt":
      message_encrypted = extensions.caesar.Caesar1.encrypt(message, 3)
      return message_encrypted
    elif mode == "decrypt":
      return extensions.caesar.Caesar1.decrypt(message, 3)
  else:
    return "Access denied"


# access with user 
def caesar2(message, mode):
  global current_role
  # Caesar 2
  if current_role == "user" or current_role == "admin":
    if mode == "encrypt":
      message_encrypted = extensions.caesar.Caesar2.encrypt(message, "halo", 3)
      return message_encrypted
    elif mode == "decrypt":
      return extensions.caesar.Caesar2.decrypt(message, 'halo', 3)
  else:
    return "Access denied"


# access with user 
def vigenere(message, mode):
  global current_role
  # Vigenere
  if current_role == "user" or current_role == "admin":
    if mode == "encrypt":
      keyword = "HALO"
      key = extensions.caesar.Vigenere.cyclic_key(message, keyword)
      message_encrypted = extensions.caesar.Vigenere.encryption(message, key)
      return message_encrypted
    elif mode == "decrypt":
      return extensions.caesar.Vigenere.decryption(message, key)
  else:
    return "Access denied"

# access with user 
def atbash(message, mode):
  global current_role
  # Atbash 
  if current_role == "user" or current_role == "admin":
    if mode == "encrypt":
      message_encrypted = extensions.caesar.Atbash.encryption(message)
      return message_encrypted
    elif mode == "decrypt":
      return extensions.caesar.Atbash.decryption(message)
  else:
    return "Access denied"


# access with user 
def Rsa(message, mode):
  global current_role
  if current_role == "user" or current_role == "admin":
    RSA = extensions.rsa.RSA()
    plain_text = message
    if mode == "encrypt":
      message_encrypted = RSA.encryption(plain_text)
      return message_encrypted
    elif mode == 'decrypt':
      message_decrypted = RSA.decryption(message)
      return str(message_decrypted)
  else:
    return "Access denied"


def perform_crud(command, key="none", value='none'):
    global users
    
    # if current_role != 'admin':
    #   return "Access denied"

    if command == "read":
      extensions.crud.CRUD.read(users, key)
      return(users.get(key))

    elif command == "create":
      extensions.crud.CRUD.create(users, key, value)
      return "data has been added"

    elif command == "update":
      extensions.crud.CRUD.update(users, key, value)
      return "data has been updated"
    
    elif command == "delete":
      extensions.crud.CRUD.delete(users, key)
      return "data has been deleted"
    
    elif command == "readAll":
      return users


@app.route('/register', methods=['GET'])
def register():
  global users

  res = request.get_json() 
  print(res)
  # {"login" : "pass"}
  for login in res:
    password = res[login]
    users[login] = password

  return "Account has been created"


@app.route('/login', methods=['GET'])
def login():
  global users
  global current_role   

  res = request.get_json() 
  print(res)
  # {"login" : "pass"}
  for login in res:
    password = res[login]
    if login == "admin" and password == "hello123":
      current_role = "admin"
      return "Entered privileged mode"
    if (login in users) and (users[login] == password):
      totp = pyotp.TOTP('base32secret3232')
      otpCode = totp.now()
      return "Confirm login by OTP code (go to /confirm and use { code : "+ otpCode + " })"

  return "Error to login"


@app.route('/logout', methods=['GET'])
def logout():
  global current_role

  current_role = 'guest'

  return "logout success"


@app.route('/confirm', methods=['GET'])
def confirm():   
  global users
  global current_role

  res = request.get_json()
  print(res) 
  # {"code" : "xxxxxx"}
  totp = pyotp.TOTP('base32secret3232')
  otpCode = totp.now()
  if res["code"] == str(otpCode):
    current_role = "user" 
    return "Welcome"
  else:
    return "OTP code wrong or expired"
      

@app.route('/cipher/<type>', methods=['GET'])
def cipher(type):   
  res = request.get_json() 
  # { 
  #   "mode" : "encrypt",
  #   "msg"  : "some-text"
  #  }

  # key_value_dict = {}
  # key_value_dict.update(res)

  if type == "caesar1":
    return(caesar1(res['msg'], res['mode']))
  elif type == "caesar2":
    return(caesar2(res['msg'], res['mode']))
  elif type == "vigenere":
    return(vigenere(res['msg'], res['mode']))
  elif type == "atbash":
    return(atbash(res['msg'], res['mode']))
  elif type == "rsa":
    return(Rsa(res['msg'], res['mode']))

  return "success"


@app.route('/users/<Command>', methods=['GET'])
def user(Command):   
  global users
  # {
  #   "key" : "login",
  #   "value" : "password"
  # }

  res = request.get_json() 

  key_value_dict = {}
  key_value_dict.update(res)

  for _key in key_value_dict:
    if _key == "login":
      key = res['login']
    elif _key == "password":
      value = res['password']

  if len(key_value_dict) == 1:    
    return(perform_crud(Command, key))
  elif len(key_value_dict) == 2:  
    return(perform_crud(Command, key, value))
  elif len(key_value_dict) == 0:
    return(perform_crud(Command))

  return users




if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=6000, use_reloader=False)