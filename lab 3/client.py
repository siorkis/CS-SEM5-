import domain

rsa = domain.RSA()
plain_text = 12345
message_encrypted = rsa.encryption(plain_text)
print(message_encrypted, "message_encrypted")
message_decrypted = rsa.decryption(message_encrypted)
print(message_decrypted, "message_decrypted")
