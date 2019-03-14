import socket
import threading

def setup():
    host = "127.0.0.1"
    port = 5001
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    
    serverClient = input("Press 'a' to join a server or 'b' to host a server")
    if serverClient.capatilise() = "A":
        ClientSetup(s)
    elif serverClient.capatilise() = "B":
        ServerSetup(s)

def ClientSetup(s):
    serverIP = input("What is the IP of the server you would like to connect to?")
    while True:
        s.sendto((":1001:"+str(name)).encode('utf-8'),(serverip,5000))
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        if data == ":2002:":
            print("Connected to ---", addr)
            ClientChatroom(s, addr)
            break

def ClientSend():

def ReceiveThread():    

def ClientChatroom(s, addr):
    sendThread = Thread(target=ClientSend)
    receiveThread = Thread(target=ReceiveThread)
    
