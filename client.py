import socket
import time


def setup():
    host = "127.0.0.1"
    port = 5001
    serverip = input("What's the ip of the server you wish to connect to?")
    name = input("What would you like to be know as on the server?")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    while True:
        s.sendto((":1001:"+str(name)).encode('utf-8'),(serverip,5000))
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        if data == ":2002:":
            print("Connected to ---", addr)
            chatroom(s, addr)
            break


def chatroom(s, server):
    message = input("-->")
    while message != "q":
        s.sendto(message.encode('utf-8'),server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received ---", data)
        message = input("-->")
    s.close()


if __name__ == '__main__':
    setup()
