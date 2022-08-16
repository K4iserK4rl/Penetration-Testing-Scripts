import socket
import threading
from queue import Queue

socket.setdefaulttimeout(0.25)

#To Avoid Multiple Modification in One Iteration
printLimit = threading.Lock()

target = input("\nEnter the Target: ")

#Resolves Given IP
targetIP = socket.gethostbyname(target)

#Port Scanner Function
print("Beginning Port Scan...\n")

def portScan(portNum):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((targetIP, portNum))
        with printLimit:
            #Checks for Well-Known Ports
            if portNum == 20:
                print("Port %s is Open (FTP)" % portNum)
            elif portNum == 21:
                print("Port %s is Open (FTP)" % portNum)
            elif portNum == 22:
                print("Port %s is Open (SSH)" % portNum)
            elif portNum == 23:
                print("Port %s is Open (Telnet)" % portNum)
            elif portNum == 25:
                print("Port %s is Open (SMTP)" % portNum)
            elif portNum == 53:
                print("Port %s is Open (DNS)" % portNum)
            elif portNum == 69:
                print("Port %s is Open (TFTP)" % portNum)
            elif portNum == 80:
                print("Port %s is Open (HTTP)" % portNum)
            elif portNum == 110:
                print("Port %s is Open (POP3)" % portNum)
            elif portNum == 143:
                print("Port %s is Open (IMAP4)" % portNum)
            elif portNum == 443:
                print("Port %s is Open (HTTPS)" % portNum)
            else:
                print("Port %s is Open" % portNum)
    
        s.close()    
    except:
        pass

#Thread Function
def threadFunction():
    while True:
        task = queue.get()
        portScan(task)
        queue.task_done()
queue = Queue()

for i in range(100):
    threads = threading.Thread(target = threadFunction)
    #Daemon Threads Run in the Background Without Disturbing Main Thread
    threads.daemon = True
    threads.start()

for task in range(1, 500):
    queue.put(task)
queue.join()
