import input_controller
from tkinter import *

class UserInterface:


    def recordBtnClick(self):
            response = input_controller.record()
            input = input_controller.parseResponse(response)
            print(input)

    def construct_buttons(self, window):
        btn = Button(window, text="Record", command=self.recordBtnClick)
        btn.grid(column=0, row=0)

    def construct_layout(self, window):
        window.title("Welcome to adLess")
        window.geometry('350x200')
        lbl = Label(window)

    def __init__(self):
        window = Tk()
        self.construct_layout(window)
        self.construct_buttons(window)
        window.mainloop()






