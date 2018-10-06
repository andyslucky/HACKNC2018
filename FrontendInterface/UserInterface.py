import input_controller
from tkinter import *


class UserInterface:

    def __init__(self):
        self.response = "asdf"
        self.window = Tk()
        self.construct_layout()
        self.construct_buttons()
        self.construct_displaytext()

        self.window.mainloop()

    def recordBtnClick(self):
<<<<<<< HEAD
        self.response = input_controller.record()
        self.construct_displaytext()
=======
        if self.isClick:
            input_controller.record()
>>>>>>> fc04fd68c3f0d85d37ef84a138e486f1d47d3dde


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










