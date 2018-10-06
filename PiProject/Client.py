
# This is code to be run on the Raspberry PI
import socket
import threading
import select

class Client:
    def __init__(self):
        self.host = "127.0.0.1"
        self.state = 1
        self.port = 2521
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__readthread = None
    def connect(self):
        self.connection.connect((self.host,self.port))
        self.__readthread = threading.Thread(target=self.read,args=tuple([]))
        self.__readthread.start()
    def setState(self,state):
        #do state stuff
        self.state = state
        return True

    def __parseinput(self,response):
        if "COMMAND" in response:
            if "0" in response:
                return self.setState(0)
            elif "1" in response:
                return self.setState(0)
        elif "GET" in response:
            if "STATE" in response:
                self.connection.sendall(str(self.state).encode("utf8"))

    def read(self):
        while True:
            rlist,wlist,errlist = select.select([self.connection],[self.connection],[self.connection],3)
            for conn in rlist:
                response = conn.recv(128)
                if response is not None and response != b"":
                    self.__parseinput(response.decode("utf8"))
                else:
                    pass

    def set_light(state):
      sendByte = ['o', 'O'][state]

    def get_light(state):
      pass

client = Client()
client.connect()
