import socket
import select
import threading
##This is the server object to be used by the front end
class Server:
    def __init__(self, response):
        #@type = Thread
        self.__listener = None
        self.host =  "0.0.0.0"
        self.port = 2521
        self.conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.response = response
        self.clients = []
    def start(self):
        self.conn.bind((self.host,self.port))
        self.__listener = threading.Thread(target=self.__listen,args=tuple([]))
        self.__listener.start()
    def __listen(self):
        self.conn.listen()
        while len(self.clients) < 4:
            client, addr = self.conn.accept()
            self.clients.append(client)
    def __scanForRead(self):
        rlist, wlist,errlist = select.select(self.clients,[],[])
        for sock in errlist:
            sock.close()
            self.clients.remove(sock)
        for sock in rlist:
            threading.Thread(target=self.__readAll,args=(sock,)).start()


    def __readAll(self,client: socket):
        response = client.recv(128)
        if response is not None and response != "":
            self.response(client,response)
        else:
            client.close()
            self.clients.remove(client)

def read(client, response):
    print(response)
s = Server(read)
s.start()