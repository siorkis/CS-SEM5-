# CRYPTOGRAPHY AND SECURITY LABORATORY WORK 4


## TOPIC: HASH FUNCTIONS AND DIGITAL SIGNATURES

Hashing is a technique used to compute a new representation of an existing value, message or any piece of text. The new representation is also commonly called a digest of the initial text, and it is a one way function meaning that it should be impossible to retrieve the initial content from the digest.

Such a technique has the following usages:

- Offering confidentiality when storing passwords,
- Checking for integrity for some downloaded files or content,
- Creation of digital signatures, which provides integrity and non-repudiation.

In order to create digital signatures, the initial message or text needs to be hashed to get the digest. After that, the digest is to be encrypted using a public key encryption cipher. Having this, the obtained digital signature can be decrypted with the public key and the hash can be compared with an additional hash computed from the received message to check the integrity of it.

## OBJECTIVES

1. Get familiar with the hashing techniques/algorithms.
2. Use an appropriate hashing algorithms to store passwords in a local DB.
    - You can use already implemented algortihms from libraries provided for your language.
    - The DB choise is up to you, but it can be something simple, like an in memory one.
3. Use an asymmetric cipher to implement a digital signature process for a user message.
    - Take the user input message.
    - Preprocess the message, if needed.
    - Get a digest of it via hashing.
    - Encrypt it with the chosen cipher.
    - Perform a digital signature check by comparing the hash of the message with the decrypted one.

## THE SHA256 ALGORITHM

In Cryptography, SHA is cryptographic hash function which takes input as 20 Bytes and rendered the hash value in hexadecimal number, 40 digits long approx.

## IMPLEMENTATION


Our local DB (memory datastore) will be just dict variable: 

My program simulates the login page of the web site. 

First, service ask user to register, he need to enter username and password. 
Username remain unchanged, meanwile password hashes using SHA-256 algoritm.

```python 
if command == "register":
    username = input("Enter new username : ")
    password = input('Enter new password: ')
    encryption_text = sha256(password.encode('utf-8')).hexdigest()
    table[username] = encryption_text
```

In our DB stores key:value pair as username and hash of the password. So when the user tries to login, he enter his password, it again hashes, and it's hash compare with DB. If thouse matches then user is able to enter the system, otherwise not.


Example: 

```md
Input : log:admin pass:newpassword123
DB    : {'admin': 'c822a0abf4ef0a5fc2a4c2010ed111e16af3ae95cee462a55e7877b8623ade36'}

Input : log:batman pass:joker555
DB    : {'batman': 'f27bee3fdd8fc42537ba8dc59f3e56ce1a861502475f75d29ec6642e95215e7b'}

Input : log:star pass:sun11
DB    : {'star': 'e8faaf31984e37a8eb1c1b5a4610b1ddc369701f0457ace3eca974369d53acea'}
```