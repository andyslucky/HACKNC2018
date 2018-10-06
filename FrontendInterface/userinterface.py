import tkinter
import run
def make_ui():
    top = tkinter.Tk()

    recordButton = tkinter.Button(top, text="Record", command = record)
    recordButton.pack()
    top.mainloop()

def record():
    run