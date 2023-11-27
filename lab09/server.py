import socket

HOST = "192.168.137.165"
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

while True:
    print("Waiting for connection...")
    conn, addr = s.accept()
    print("Add connection from" + str(addr))

    while True:
      indata = conn.recv(1024)

      result = 0
      list = []

      if (len(indata) == 0) or (indata.decode() == 'exit'):
          print("connection closed")
          conn.close()
          break
      else:
        print("Received from" + str(addr) + ": ", indata.decode())
        for i in range(int(indata.decode())+1):
           if i ==0:
               a = 0
           elif i == 1:
               a = 1
               list = [0, 1]
           else:
               a = list[0] + list[1]
               del list[0]
               list.append(a)

        outdata = str(a)
        conn.send(outdata.encode())
        print("Send to " + str(addr) + ": " + str(a))