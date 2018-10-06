
# This is code to be run on the Raspberry PI
import socket
import select

import serial

class Client:
    def __init__(self):
        self.host = "127.0.0.1"
        self.state = 0
        self.port = 2521
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__readthread = None
        self.COM = self.getDevice("/dev/tty.usbmodem")
        self.ser = serial.Serial(COM)

    def connect(self):
        self.connection.connect((self.host,self.port))
        self.__readthread = threading.Thread(target=self.read,args=tuple([]))
        self.__readthread.start()

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

    def getDevice(self, beginsWith):
        for dev in list(os.walk("/dev"))[0][2]: #shhh don't ask why
            if '/dev/' + dev[:len(beginsWith)-5] == beginsWith:
                return '/dev/' +dev
        raise Exception("Radio controller not connected")

    def set_light(self, state):
        sendByte = [b'o', b'O'][state]
        self.ser.write(sendByte)
        self.ser.flush()

        self.state = state
        return True

    def get_light(self, state):
        pass

client = Client()
client.connect()

import time

time.sleep(0.855396)
client.toggle_light()
time.sleep(1.116571)
client.toggle_light()
time.sleep(1.351903)
client.toggle_light()
time.sleep(1.849650)
client.toggle_light()
time.sleep(2.330630)
client.toggle_light()
time.sleep(2.838812)
client.toggle_light()
time.sleep(3.076490)
client.toggle_light()
time.sleep(3.309356)
client.toggle_light()
time.sleep(3.760542)
client.toggle_light()
time.sleep(4.245208)
client.toggle_light()
time.sleep(4.645607)
client.toggle_light()

