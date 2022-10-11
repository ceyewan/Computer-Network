from socket import *
import time

serverAddr = ("localhost", 12000)
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(10):
    message = "ceyewan"
    start = time.time()
    clientSocket.sendto(message.encode(), serverAddr)
    try:
        response, _ = clientSocket.recvfrom(1024)
    except timeout:
        print("Request timeout!")
        continue
    end = time.time()
    print(f"RTT {i}: {(end - start)*1000} ms")
