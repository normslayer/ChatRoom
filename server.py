import socket

clients = []

def Main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        if data[:6] == ":1001:":
            clients.append([addr,data[:-6]])
            s.sendto(":2002:".encode('utf-8'), addr)
            break
        print("Message From: " + str(addr))
        print("From Connected User:" + data)
        data = data.upper()
        print("Sending:",data)
        s.sendto(data.encode('utf-8'), addr)
    s.close()

if __name__ == '__main__':
    print(socket.gethostbyname(socket.gethostname()))
    Main()
    
