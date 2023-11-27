import socket

HOST = "192.168.137.165"
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("connected to " + HOST)

while True:
    outdata = input("The Fabonnaci(n) when n = ")
    s.send(outdata.encode())

    indata = s.recv(1024)
    if (len(indata) == 0):
        s.close()
        print('Connection Closed.')
        break
    print("the ans is " + indata.decode())
s.close()