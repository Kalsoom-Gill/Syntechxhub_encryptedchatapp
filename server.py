import socket
import threading
from encryption import decrypt_message

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print(f"Server started on {HOST}:{PORT}")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

def handle_client(client, address):
    print(f"{address} connected.")

    while True:
        try:
            encrypted_message = client.recv(1024)

            if not encrypted_message:
                break

            message = decrypt_message(encrypted_message)

            print(f"{address}: {message}")

            with open("chat_log.txt", "a") as log:
                log.write(f"{address}: {message}\n")

            broadcast(encrypted_message, client)

        except:
            break

    print(f"{address} disconnected.")

    if client in clients:
        clients.remove(client)

    client.close()

while True:
    client, address = server.accept()

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()