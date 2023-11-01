from socket import *
from time import ctime, time
import os, traceback, logging


HOST = 'localhost'
PORT = 8000
ADDRESS = (HOST, PORT)


server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
print("Waiting for Connection ...")



def errorHandling(error):
    logging.error(traceback.format_exc())
    print(error)
    socket.close()



def getConnection():
    try:
        client, address = server.accept()

    except Exception as ERROR:
        errorHandling(ERROR)

    else:
        print("... connected from: ", address)
        return [client, address]



def readImage(path, client):
    try:
        with open(path, "rb") as image_file:
            image_data = image_file.read()

    except Exception as ERROR:
        errorHandling(ERROR)

    else:
        # Send the image data
        client.sendall(image_data)

    finally:
        return



def getFile(client, address, data):
    currDirectory = os.getcwd()
    imgPath = currDirectory + '/images/' + data

    print("Loading file from disk at location: ", imgPath)
    print("Sending file to client at: ", address)

    readImage(imgPath, client)

    print(f"Sent a total of {os.path.getsize(imgPath)} bytes")
    

    return 



def clientRequest(client, address):
    try:
        data = client.recv(1024).decode("utf-8")

    except Exception as ERROR:
        errorHandling(ERROR)
    
    else:
        print("Recieved a request file: ", str(data))

        getFile(client, address, str(data))


        return 



while True:
    package = getConnection()

    clientRequest(package[0], package[1])

    print("CLOSING SERVER AT: ", package[1])

    server.close()
    break



