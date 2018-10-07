
import Langprocessor_controller
import input_controller
from tkinter import *
import Server
import input_lang_controller
import threading

class UserInterface:

    def __init__(self):
        self.listeningThread = None
        self.response = "asdf"
        self.lbl = None
        self.deviceAddr = None
        self.server = Server.Server(self.read,self.connected,self.disconnected)
        self.server.start()
        self.window = Tk()
        self.construct_layout()
        self.construct_buttons()
        self.construct_displaytext("Not-Listening")
        self.window.mainloop()
    def read(self,client,response):
        pass
    def connected(self,addr):
        self.deviceAddr = addr
        print("addr connected "+str(addr))
        pass
    def disconnected(self,addr):
        pass
    def recordBtnClick(self):

        if self.listeningThread is None:
            self.setIndicatorText("Recording")
            self.listeningThread = threading.Thread(target=input_controller.record,args=(self.dostuff,self))
            self.listeningThread.start()
        else:
            pass



    def dostuff(self,input):
        self.response = str(input)
        self.server.setState(self.deviceAddr, 1 if input else 0)
        # input_lang_controller.commands(self.response)
        self.setIndicatorText(self.response)

    def construct_buttons(self):
        btn = Button(self.window, text="Record", command=self.recordBtnClick)
        btn.grid(column=0, row=0)

    def construct_layout(self):
        self.window.title("Welcome to adLess")
        self.window.geometry('350x200')
    def setIndicatorText(self,text):
        self.lbl.configure(text=text)
    def construct_displaytext(self,text):
        resp = text
        print(resp)
        self.lbl = Label(self.window, text="Not-Listening")
        self.lbl.grid(column=0, row=1)