from datetime import datetime
from tkinter import *
root=Tk()
def dis():
    d1=datetime.today()
    l1.config(text=d1.strftime("%H:%M:%S"))
    l1.after(1000,dis)
root.geometry("400x400")
l1=Label(root)
l1.pack()
dis()
root.mainloop()