from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive: ")
while True:
    message, clientAdress = serverSocket.recvfrom(2048)
    modifyMessaages = message.decode().upper()
    serverSocket.sendto(modifyMessaages.encode(), clientAdress)