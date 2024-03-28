"""
goal: parse HTTP request, format headers in JSON, serve back
"""

import json
import socket

HOST = '0.0.0.0'
PORT = 7771

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen()
print('Listening for new connections on port ', PORT)

while True:
    conn, addr = s.accept()
    # for any given connection, continue receiving data until data stops arriving
    print(f'New connection from address {addr}')
    req = conn.recv(4096) # TODO keep calling recv
    headers, body = req.split(b'\r\n\r\n')
    d = {}
    for hline in headers.split(b'\r\n')[1:]:
        k, v = hline.split(b': ')
        d[k.decode('ascii')] = v.decode('ascii')
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    conn.send(json.dumps(d, indent=4).encode('ascii'))
    conn.close()