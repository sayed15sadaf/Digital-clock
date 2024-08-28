from tkinter import *
import time

win = Tk()
win.configure(bg="#D4F1F4")
win.title("Digital Clock")
win.geometry("600x180")
win.resizable(0,0)

def present_time():
    currentTime = time.strftime("%I:%M:%S %p")
    
    labelTime.configure(text=currentTime)
    labelTime.after(1000, present_time)
    
timeString = time.strftime('%H:%M:%S')

labelTime = Label(text=f"{timeString}", fg="#76B947", bg="#D4F1F4", font=("Arial 35 bold"))
labelTime.pack(expand=True)

present_time()
win.mainloop()