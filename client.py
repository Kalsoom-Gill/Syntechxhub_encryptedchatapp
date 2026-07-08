import socket
import threading
from encryption import encrypt_message, decrypt_message

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to Server!")

def receive_messages():
    while True:
        try:
            encrypted_message = client.recv(1024)

            if not encrypted_message:
                break

            message = decrypt_message(encrypted_message)
            print("\nFriend:", message)

        except:
            print("Disconnected from server.")
            break

def send_messages():
    while True:
        message = input("You: ")

        encrypted_message = encrypt_message(message)
        client.send(encrypted_message)

        if message.lower() == "exit":
            client.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

send_messages()