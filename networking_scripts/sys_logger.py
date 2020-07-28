'''
Just run "python3 sys_logger.py"

configure your device to send UDP logs to the host, and Enjoy :)
'''


import socket

HOST = '0.0.0.0'
PORT = 514

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"{HOST} Listening on port {PORT}")

    while True:
        data = s.recv(1024)
        print(data)
        if not data:
            break

