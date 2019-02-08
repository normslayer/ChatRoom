import socket

def Main():
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1',5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    while True:
        serverAddress = input("What is the ip of the server?")
        s.sendto(":1001:".encode('utf-8'),(serverAddress,5000))
        data, addr = s.recvfrom(1024)
        if data == ":2002:":
            print("Connected to", addr)
            #todo break here and move to the chating bit

    message = input("-->")
    while message != "q":
        s.sendto(message.encode('utf-8'),server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Recieved from server:", data)
        message = input("-->")
    s.close()

if __name__ == '__main__':
    Main()
