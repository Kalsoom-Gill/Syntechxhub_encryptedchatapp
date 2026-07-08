from cryptography.fernet import Fernet

with open("key.key", "rb") as file:
    secret_key = file.read()

cipher = Fernet(secret_key)

def encrypt_message(message):
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message).decode()