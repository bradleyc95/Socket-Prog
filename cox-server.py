'''
UDP Server
Bradley Cox, 10/11/2022
Requests a string from the client, and returns the sum of ordinal values of each character
'''

from socket import *

serverHost = 'localhost'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind((serverHost,serverPort))

print('The server is ready to receive...')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    asciiSum = 0
    modifiedMessage = message.decode()
    # print(modifiedMessage)
    for char in modifiedMessage:
        asciiSum += ord(char)
    modifiedMessage = str(asciiSum)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
