#+TITLE: CRYPTOGRAPHY AND SECURITY LABORATORY WORK 5
#+AUTHOR: FCIM FAF-203 Covtun Serghei


** TOPIC:  Web Authentication & Authorisation

 Authentication & authorization are 2 of the main security goals of IT systems and should not be used interchangibly. Simply put, during authentication the system verifies the identity of a user or service, and during authorization the system checks the access rights, optionally based on a given user role.

** OBJECTIVES

1. Take what you have at the moment from previous laboratory works and put it in a web service / serveral web services.
2. Your services should have implemented basic authentication and MFA (the authentication factors of your choice).
3. Your web app needs to simulate user authorization and the way you authorise user is also a choice that needs to be done by you.
4. As services that your application could provide, you could use the classical ciphers. Basically the user would like to get access and use the classical ciphers, but they need to authenticate and be authorized. 

** IMPLEMENTATION

For a client side we will use Postman 

First I have implemented registration system 
Web server (with flask framework) have 4 different routs for that purpose.

1. Register
2. Login 
3. Confirm
4. Logout

** Register

```python 
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
```

User provide a request with specific JSON format and then new user added to the local memory data store ("users" variable)

```
{ "login" : "password" }
```

** Login 

```python 
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

```

User provide a request with specific JSON format and then system check if such user is present in the local DB. If yes, then user gets OTP code which should be used in order to complete login process. 

```
{ "login" : "password" }
```

** Confirm 

```python 
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
```
User provide a request with specific JSON format and then system check if OTP code is correct and don't expired yet. System grants the role "user" to the guest in case of success.

```
{ "code" : "123456" }
```

** Logout 

```python 
@app.route('/logout', methods=['GET'])
def logout():
  global current_role

  current_role = 'guest'

  return "logout success"
```

Finally each user could logout from the system and it grants him role "guest". 

** Roles 

In that system exist 3 roles which defines access to a different tools. 
- guest 
Guests simply could use only registration functionality.
- user
Users are not privileged ones, they could only encrypt/decrypt messages by using one of the ciphers
- admin 
Admin is the user with full access to the system, which includes managing local DB of all users and performing CRUD (create, read, delete, update) operations on it.

** Ciphers 

In this lab work was implemented ciphers which encrypt only text messages and 1 additional cypher for numbers (RSA)

- 2 types of caesar 
- vigenere
- atbash 
- rsa

Users could use route ../cipher/ and select type of it (caesar1, caesar2, vigenere, atbash or rsa) in order to get access to one of them 

Ex: .../cipher/caesar1

And provide JSON with following format:

mode: encrypt/decrypt 
msg: plain-text/encrypted-text

```
{ 
   "mode" : "encrypt", 
   "msg"  : "some text"
}
```

** Local DB 

If user login with pre-defined login: "admin" and password: "hello123", then system grants role "admin" to that user. With role "admin" you could perform CRUD operations.

For that purpose exist route ../users/ and specified commands: 
- read
return password of the user by sending JSON request:

```
{ "login" : "batman" }
```
- readAll
User can provide nothing in request and get response with all content of DB in JSON format 
- create
Creates new user with indicated login and password
```
{
    "login" : "batman",
    "password" : "123456"
}
```
- update 
Updates the password of indicated user
```
{
    "login" : "batman",
    "password" : "new123"
}
```
- delete 
Delete user with indicated login

```
{
    "login" : "batman"
}

Ex: ../users/create
```
{
    "login" : "batman",
    "password" : "123456"
}
```
