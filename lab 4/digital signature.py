import rsa
from hashlib import sha256
import RSA


message = "Trust no one"
encryption_text = sha256(message.encode('utf-8')).hexdigest()
print(encryption_text, "hash")

number_hash = hash(encryption_text)
print(number_hash,  "number from hash")

# Message to be encrypted
msg = number_hash
print("Message data = ", msg)
rsa = RSA.RSA()
message_encrypted = rsa.encryption(msg)
digital_sign = rsa.decryption(msg)

print(digital_sign, "digital signature")

message_decr = rsa.encryption(digital_sign)

