__author__ = 'jdemp'
from socket import*
serverName = 'localhost'
serverPort = 8002
clientSocket = socket(AF_INET,SOCK_DGRAM)
sensor_name = ''

message = input('Input lowercase sentence: ')
message = sensor_name + ':' + message

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage,serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()