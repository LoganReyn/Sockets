""" Server Socket Test. """

from hashlib import sha512
from functions import (ServerSocket,
                        getLogger,
                        chunkFile,
                        ENCODING)

PORT: int = 55_110

logger = getLogger("ServerLog.log")

with ServerSocket(PORT) as sock:
    
    connection, address = sock.accept()

    with connection:

        print(f"Client Connected {address}")
        connection.sendall(b"ready")

        fileName = connection.recv(1_000).decode()
        print(f"Preparing to recive file: {fileName}")

        fileSize = connection.recv(1_000).decode()
        print(f"Preparing to recive number of bytes: {fileSize}")

        myFile = chunkFile(connection, int(fileSize))
        print(f"File Recived from Client {fileName}")

        fHash = sha512(myFile).hexdigest()
        connection.sendall(bytes(fHash, ENCODING))
        print(f"Hash written to file: {fHash}")