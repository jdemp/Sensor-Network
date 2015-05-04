__author__ = 'jdemp'
from socket import*
import time
import logging
serverPort = 8002
serverSocket = socket(AF_INET, SOCK_DGRAM)
sensor_name = ''
serverSocket.bind(('', serverPort))

print('The server is ready to receive')

logging.basicConfig(filename='pi.log', format='%(asctime)s %(message)s', datefmt='%d-%m-%Y %H:%M',
                    level=logging.INFO)
logging.info('Started')

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    message_decode = message.decode()
    client = message_decode.split(':')[0]
    request = message_decode.split(':')[1]
    logging.info('REQUEST from ' + client + ' | ' + request)
    modifiedMessage = sensor_name + ':' + request.upper() + ' ' + time.strftime('%d-%m-%Y %H:%M')
    logging.info('RESPONSE to ' + client + ' | ' + modifiedMessage)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
