import socket

HOST = "192.168.137.165" #初始化設定
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("connected to " + HOST)

while True: #傳出要計算的data
    outdata = input("The Fabonnaci(n) when n = ")
    s.send(outdata.encode())

    indata = s.recv(1024) #接收計算過後的data
    if (len(indata) == 0):
        s.close()
        print('Connection Closed.')
        break
    print("the ans is " + indata.decode())
s.close()