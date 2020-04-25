from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)    # 使用tcp连接
clientSocket.connect((serverName, serverPort))
sentence = input("Input lowercase sentence: ")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("from server: {}".format(modifiedSentence))
clientSocket.close()