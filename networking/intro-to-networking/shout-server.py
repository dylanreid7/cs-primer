import socket

HOST = '0.0.0.0'
PORT = 9999
# set up the socket initially with the default family and DGRAM as the type
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the socket to host 0.0.0.0 (all IPv4 addresses on the local machine) and PORT 9999 (randomly selected, unused port)
s.bind((HOST, PORT))
# server should always be running, as that's what servers do
while True:
    # get the msg and sender of any requests to this host/port
    msg, sender = s.recvfrom(4096)
    # send the message back to the sender, uppercased
    s.sendto(msg.upper(), sender)