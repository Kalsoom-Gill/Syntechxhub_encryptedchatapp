from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as file:
        file.write(key)

    print("AES Key Generated Successfully!")

if __name__ == "__main__":
    generate_key()