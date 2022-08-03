from tkinter import *
from tkinter import colorchooser


window = Tk()
window.geometry("420x420")
button = Button(text="Click",
                padx=60,
                pady=30,
                font=("Arial",20),
                bg="red",
                fg="white",
                relief="ridge",
                command="click")
button.place(x=120,y=140)

window.mainloop()