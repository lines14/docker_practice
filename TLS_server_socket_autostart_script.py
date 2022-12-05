# to enable autostarting use bash commands:
# sudo systemctl enable server_socket_autostart_script.service
# sudo systemctl start server_socket_autostart_script.service

# to check working status use bash command:
# sudo systemctl status server_socket_autostart_script.service

import ssl
import socket
import stun
import os
import dotenv

# # блок исключений для работы в паблике с неверифицированными сертификатами:

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     # Legacy Python that doesn't verify HTTPS certificates by default
#     pass
# else:
#     # Handle target environment that doesn't support HTTPS verification
#     ssl._create_default_https_context = _create_unverified_https_context

# loading created .env file from Python PATH with login variables:

dotenv.load_dotenv()

# get() в случае отсутствия входящих данных выводит None вместо ошибки:

INTERNAL_HOST_IP = os.environ.get('INTERNAL_HOST_IP')
SOCKET_PORT = os.environ.get('SOCKET_PORT')
SOCKET_PORT = int(SOCKET_PORT)

out = f'connected to {stun.get_ip_info()[1]} => {INTERNAL_HOST_IP}\nПакет возвращён успешно: '

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/home/lines14/projects/Server-chain-certificate.pem', '/home/lines14/projects/Server-private-key.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_side=True) as ssock:
        ssock.bind(('', SOCKET_PORT))
        ssock.listen(5)

        while True:
            conn, addr = ssock.accept()

            with conn:
                print(f'Connected by {addr}')   

                while True:
                    inn = conn.recv(1024)
                    if not inn:
                        break
                    ssock_version = f'{conn.version()} '
                    conn.sendall(ssock_version.encode() + out.encode() + inn)