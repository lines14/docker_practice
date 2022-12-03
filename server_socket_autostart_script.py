# to enable autostarting use bash commands:
# sudo systemctl enable server_socket_autostart_script.service
# sudo systemctl start server_socket_autostart_script.service

# to check working status use bash command:
# sudo systemctl status server_socket_autostart_script.service

import socket
import stun
import os
import dotenv

# loading created .env file from Python PATH with login variables:

dotenv.load_dotenv()

# get() в случае отсутствия входящих данных выводит None вместо ошибки:

INTERNAL_HOST_IP = os.environ.get('INTERNAL_HOST_IP')
SOCKET_PORT = os.environ.get('SOCKET_PORT')
SOCKET_PORT = int(SOCKET_PORT)

out = f'Connected to {stun.get_ip_info()[1]} => {INTERNAL_HOST_IP}\nПакет возвращён успешно: '

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('', SOCKET_PORT))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()

        with conn:
            print(f'Connected by {addr}')   

            while True:
                inn = conn.recv(1024)
                if not inn:
                    break
                conn.sendall(out.encode() + inn)