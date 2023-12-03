import socket
import threading

class ThreadedServer(object): #建立ThreadedServer種類
    def __init__(self, host, port): #建構式
        self.host = host #初始化設定
        self.port = port
        host = "192.168.137.165"
        port = 8000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self): #建立Function偵測接受到訊息
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print("Add connection from" + str(address))
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start() #將新連接的client建立新的子執行

    def listenToClient(self, client, address): #建立Function接受到Client訊息
        while True:
            try:
                indata = client.recv(1024)
                if indata:
                    response = indata
                    client.send(response)
                else:
                    pass
            except:
                client.close()
                return False

if __name__ == "__main__": #當該檔案執行時執行
    print("Waiting for connetion...")
    while True:
        port_num = 8000
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen() #執行上述分類
