#Write Python GUI program to take accept your birthdate and output your age when a button is pressed
from tkinter import *
from datetime import date
w=Tk()
def dis():
    s1=e1.get()
    s2=s1.split('/')
    d1=date.today()
    d1=str(d1)
    d1=d1.split('-')
    age=int(d1[0])-int(s2[2])
    l1.config(text=age) 
w.geometry("400x500")
l1=Label(w,text="enter your birthdate by /")
l1.pack()
e1=Entry(w)
e1.pack()
l2=Label(w)
l2.pack()
b1=Button(w,text="calculate age",command=dis)
b1.pack()
w.mainloop()