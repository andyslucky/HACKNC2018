import socket
import select
import threading
##This is the server object to be used by the front end
class Server:
    def __init__(self, response,clientconnected, clientdisconnected):
        #@type = Thread
        self.__listener = None
        self.__reader = None
        self.host = "0.0.0.0"
        self.port = 2521
        self.conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.response = response
        self.clientconnected = clientconnected
        self.clientdisconnected = clientdisconnected
        self.clients = []
    def start(self):
        self.conn.bind((self.host,self.port))
        self.__listener = threading.Thread(target=self.__listen,args=tuple([]))
        self.__reader = threading.Thread(target=self.__scanForRead,args=tuple([]))
        self.__reader.start()
        self.__listener.start()
    def __close(self,client):
        client.close()
        #print("Closing connection " + client.getpeername())
        self.clients.remove(client)
        self.clientdisconnected(client.getpeername())
    def __listen(self):
        self.conn.listen()
        while len(self.clients) < 4:
            client, addr = self.conn.accept()
            self.clients.append(client)
            self.clientconnected(addr)
    def __scanForRead(self):
        while True:
            for conn in self.clients:
                if conn.fileno() == -1:
                    self.clients.remove(conn)
            if len(self.clients) == 0:
                continue

            rlist, wlist,errlist = select.select(self.clients,self.clients,self.clients,3)
            for sock in errlist:
                self.__close(sock)
            for sock in rlist:
                threading.Thread(target=self.__readAll,args=(sock,)).start()
    def connectedClients(self):
        return [c.getpeername() for c in self.clients]
    def __sendMsg(self,addr,message:str):
        for client in self.clients:
            if client.getpeername() == addr:
                client.sendall(message.encode("utf8"))
                print("Sent "+message)
                return
        print("Client not connected!")

    def __readAll(self,client: socket):
        try:
            response = client.recv(128)
            if response is not None and response != b"":
                self.response(client,str(response))
            else:
                self.__close(client)
        except:
            client.close()
            pass
    def setState(self,addr,state):
        self.__sendMsg(addr,"COMMAND "+str(state))
        pass
    def getState(self,addr):
        self.__sendMsg(addr,"GET STATE")
        # raise ValueError("Shit happened")
    def __del__(self):
        self.conn.close()
