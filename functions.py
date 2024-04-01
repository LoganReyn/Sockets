""" Functions and Classes for Assignment 11/12. """

import socket
import logging
from hashlib import sha512

ENCODING: str = "utf-8"

def getLogger(logFileName: str) -> logging.Logger:
    """ Basic Setup for Logger Object. """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(logFileName)
    formater = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formater)
    logger.addHandler(handler)
    return logger.info("Logger Created")
    
def chunkFile(connection, fileSize):
    """ Recive stream in 4kb chunks. """
    data = b""
    dataLen = 0 
    while dataLen < fileSize:
        chunk = connection.recv(4_000)
        if chunk:
            data += chunk
            dataLen += len(chunk)
        else:
            break
    return (data)


## Classes ##

class File:

    def __init__(self, filePath) -> None:
        self.setFileName(filePath)
        self.setBinary(filePath)
        self.setLength()

    def setFileName(self, filePath:str) -> None:
        try:
            name = filePath.split("\\")[-1]
            self.__fileName = name
        except IndexError: 
            self.__fileName = filePath 
        except Exception:
            raise Exception
        
    def setLength(self) -> None:
        self.__length = len(self.__binary)
        
    def setBinary(self, filePath) -> None:
        with open(filePath, "rb") as file:
            self.__binary = file.read()

    def getBinary(self) -> bytes:
        return self.__binary
    
    def getFileName(self) -> bytes:
        return self.__fileName
    
    def getLength(self) -> str:
        return str(self.__length)


def _typeCheck(type, *args) -> None:
    for arg in args:
        if not isinstance(arg, type):
            raise TypeError
        else:
            return None

class DefultSocket(socket.socket):

    def __init__(self, port: int) -> None:
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.setPort(port)
        self.__host = socket.gethostname()

    def setPort(self, portNumber: int):
        _typeCheck(int, portNumber)
        if portNumber < 2_000 or portNumber > 65_000:
            raise ValueError
        self.__port = portNumber

    def setHost(self, host):
        self.__host = host

    def getHost(self):
        return self.__host
    
    def getPort(self):
        return int(self.__port)
    
class ClientSocket(DefultSocket):

    def __init__(self, port: int, host) -> None:
        super().__init__(port)
        self.setHost(host)
        self.connect((self.getHost(), self.getPort()))
    
class ServerSocket(DefultSocket):

    def __init__(self, port) -> None:
        super().__init__(port)
        self.bind((self.getHost(), self.getPort()))
        self.listen()
        print(f"Server is listening on {self.getHost()}:{self.getPort()}")