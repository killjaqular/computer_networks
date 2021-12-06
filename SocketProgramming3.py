import socket
from datetime import datetime

from sys import stdout

HOST = "35.231.27.109"
PORT = 32123

MESSAGE = "TIME"

timeBefore = datetime.now()

UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

while True:
    UDPSocket.sendto(MESSAGE.encode('utf-8'), (HOST, PORT))

    reply, _ = UDPSocket.recvfrom(4096)

    timeAfter = datetime.now()

    timeReceived = reply.decode('utf-8')

    date, time = timeReceived.split(" ")
    year, month, day = [int(x) for x in date.split("-")]
    hour, minute, seconds = time.split(":")
    hour, minute = (int(hour) - 5), int(minute)
    seconds, milli = [int(x) for x in seconds.split(".")]

    timeReceived = datetime(year, month, day, hour, minute, seconds, milli)

    if len(reply) > 0: break

UDPSocket.close()

stdout.write(f"Time Before:   {timeBefore}\n")
stdout.write(f"Time Received: {timeReceived}\n")
stdout.write(f"Time After:    {timeAfter}\n")

RTT = timeAfter - timeBefore
average = (RTT / 2) + timeBefore
timeDifference = timeReceived - average

stdout.write(f"\nRTT:  {RTT}\n")
stdout.write(f"\nTime Differnece:  {timeDifference}\n")
