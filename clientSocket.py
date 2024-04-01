""" Client Socket Test. """

import time
from functions import (ClientSocket,
                       getLogger,
                       ENCODING,
                       File)


PORT: int = 55_110
HOST: str = "184.72.100.107"

logger = getLogger("ClientLog.log")


with ClientSocket(PORT, HOST) as sock:

    ready = sock.recv(1_000)

    if ready:

        filePath = input("Path of File\n")

        myFile = File(filePath)

        ### SEND #
        sock.sendall(bytes(myFile.getFileName(), ENCODING)); time.sleep(2)

        # send file length
        sock.sendall(bytes(myFile.getLength(), ENCODING)); time.sleep(2)

        # send file
        sock.sendall(myFile.getBinary()); time.sleep(2)

        ### RECIVE #
        serverHash = sock.recv(250).decode()
        print(f"Hash recived from server: {serverHash}")

print ("Client Done")