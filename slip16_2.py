#  Write Python GUI program to add items in listbox widget and to print and delete the
# selected items from listbox on button click. Provide three separate buttons to add, print
# and delete.
from tkinter import *
from tkinter import messagebox
root=Tk()
def dis():
    l1.insert(0,e1.get())
def dis1():
    s1=l1.curselection()
    l1.delete(s1)
def dis2():
    
    messagebox.showinfo("list",l1.get(0,5))
root.geometry("500x500")
l1=Listbox(root)
l1.pack()
e1=Entry(root)
e1.pack()
b1=Button(root,text="add",command=dis)
b2=Button(root,text="print",command=dis2)
b3=Button(root,text="delete",command=dis1)
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
