import socket
import time

def Main():
    server = ('127.0.0.1',5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    
    serverAddress = input("What is the ip of the server?")
    while True:        
        s.sendto(":1001:".encode('utf-8'),(serverAddress,5000))
        data, addr = s.recvfrom(1024)
        if data == ":2002:":
            print("Connected to", addr)
            break
        else:
            print(data.decode())

    message = input("-->")
    while message != "q":
        s.sendto(message.encode('utf-8'),server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server:", data)
        message = input("-->")
    s.close()

def setup():
    host = socket.gethostbyname((socket.gethostbyname()))
    port = "5001"
    serverip = input("What's the ip of the server you wish to connect to?")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    while True:
        s.sendto(":1001:").encode('utf-8'),(serverip,5000)
        time.sleep(0.5)
        data, addr = s.recvfrom(1024)
        if data == ":2002":
            print("Connected to ---", addr)
            chatroom(s, addr)
    s

def chatroom(s):

if __name__ == '__main__':
    Main()
