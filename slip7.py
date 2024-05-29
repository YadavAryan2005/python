# Write python GUI program to generate a random password with upper and lower
# case letters.
import random
import string
from tkinter import *
root=Tk()
def dis():
    s=string.ascii_lowercase+string.ascii_uppercase
    s1=random.choices(s,k=10)
    l1.configure(text=s1)
root.geometry("400x400")
l1=Label(root)
l1.pack()
b1=Button(root,text="generate random password",command=dis)
b1.pack()
root.mainloop()