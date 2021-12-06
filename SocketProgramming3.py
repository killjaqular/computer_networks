import socket
import sys

HOST = "35.231.27.109"
PORT = 23185

MESSAGE = "LIST"
print("UDP PACKET")
UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
while True:
    UDPSocket.sendto(MESSAGE.encode('utf-8'), (HOST, PORT))
    reply, address = UDPSocket.recvfrom(4096)
    print(reply.decode('utf-8'))
    if len(reply) > 0: break

UDPSocket.close()
