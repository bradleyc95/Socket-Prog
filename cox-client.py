'''
UDP Client
Bradley Cox, 10/11/2022
Requests a string from the client, and returns the sum of ordinal values of each character
'''

from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Enter a sentence to receive the sum of each character\'s ascii value: ')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()
