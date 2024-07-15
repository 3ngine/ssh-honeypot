import socket
import threading
import paramiko
import logging

#Port that this uses, by default its 22. Change it if needed
port = 22

# Here's the log file, you can modify it however you want
logging.basicConfig(filename="logs.log", level=logging.INFO, format='%(asctime)s - %(message)s')

host_key = paramiko.RSAKey(filename='GENERATED_RSA_KEY.key')

class HoneypotSSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        logging.info(f"Login attempt with username: {username}, password: {password}")
        return paramiko.AUTH_FAILED

def handle_client(client_socket, client_address):
    try:
        transport = paramiko.Transport(client_socket)
        transport.add_server_key(host_key)
        server = HoneypotSSHServer()

        transport.start_server(server=server)

        channel = transport.accept(20)
        if channel is None:
            raise Exception("No channel was created")

        channel.send("Welcome to SSH honeypot!\r\n")
        channel.close()
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
    finally:
        transport.close()

def start_honeypot():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", port))
    server_socket.listen(100)

    logging.info(f"SSH Honeypot is running on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        logging.info(f"Connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_honeypot()
