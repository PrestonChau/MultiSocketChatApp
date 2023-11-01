
from socket import *
from time import ctime
import os

HOST = 'localhost'
PORT = 8000
ADDRESS = (HOST, PORT)
BUFFSIZE = 240689


client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDRESS)


fName = input("Enter the file name of the image, with its extension: ")
client.send(bytes(fName, 'utf-8'))

currDirectory = os.getcwd()
imgPath = currDirectory + '/images/recieved.jpg'


with open(imgPath, "wb") as image_file:
    while True:
        # Receive data from the client
        data = client.recv(1024)
        if not data:
            break
        # Write the received data to the file
        image_file.write(data)

print("File recieved, total bytes: ", os.path.getsize(imgPath))

print("File saved as recieved.jpg")


client.close()
