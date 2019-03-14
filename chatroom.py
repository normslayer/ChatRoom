import socket

def setup():
    host = "127.0.0.1"
    port = 5001
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    
    serverClient = input("Press 'a' to join a server or 'b' to host a server")
    if serverClient.capatilise() = "A":
        Client()
    elif serverClient.capatilise() = "B":
        Server()
