from hashlib import sha256

table = {}
command = input("Enter command (login, register, exit): ")
while command != 'exit':
    if command == "register":
        username = input("Enter new username : ")
        password = input('Enter new password: ')
        encryption_text = sha256(password.encode('utf-8')).hexdigest()
        table[username] = encryption_text
    elif command == "login":
        username = input("Enter username : ")
        password = input("Enter password: ")
        check_hash = sha256(password.encode('utf-8')).hexdigest()
        if table[username] == check_hash:
            print("Welcome")
        else:
            print("Wrong password")

    command = input("Enter command (login, register, exit): ")
