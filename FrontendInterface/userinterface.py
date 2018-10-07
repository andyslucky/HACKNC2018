import Langprocessor_controller
import input_controller
from tkinter import *
import Server
import input_lang_controller


class UserInterface:

    def __init__(self):
        self.response = "asdf"
        self.deviceAddr = None
        self.server = Server.Server(self.read,self.connected,self.disconnected)
        self.server.start()
        self.window = Tk()
        self.construct_layout()
        self.construct_buttons()
        self.construct_displaytext()
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
        val = input_controller.record()

        self.response = str(val)
        self.server.setState(self.deviceAddr,1 if val else 0)
        #input_lang_controller.commands(self.response)
        self.construct_displaytext()


    def construct_buttons(self):
        btn = Button(self.window, text="Record", command=self.recordBtnClick)
        btn.grid(column=0, row=0)

    def construct_layout(self):
        self.window.title("Welcome to adLess")
        self.window.geometry('350x200')

    def construct_displaytext(self):
        resp = self.response
        print(resp)
        lbl = Label(self.window, text=self.response)
        lbl.grid(column=0, row=1)
        pass










