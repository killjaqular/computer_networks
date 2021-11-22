import socket
import sys

HOST = "35.231.27.109"
PORT = 23185

MESSAGE = "apichardo2019"
print("UDP PACKET")
UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
while True:
    UDPSocket.sendto(MESSAGE.encode('utf-8'), (HOST, PORT))
    reply, address = UDPSocket.recvfrom(4096)
    print(reply.decode('utf-8'))
    if len(reply) > 0: break

UDPSocket.close()

HOST = b"google.com"
PORT = 80

print("TCP PACKET")
TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

TCPSocket.connect((HOST, PORT))
TCPSocket.sendall(b"GET / HTTP/1.1\r\nHost: " + HOST + b":" + bytearray(str(PORT), "utf-8") + b"\r\n\r\n")
reply = TCPSocket.recv(4096)
print(reply)

TCPSocket.close()
