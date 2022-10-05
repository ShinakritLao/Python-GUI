from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
from tkinter import ttk
import tkinter.messagebox
import sys

myScreen = Tk()
myScreen.title("My GUI")
myScreen.geometry("500x500")

def showConfirm():
    status = tkinter.messagebox.askyesno("Confirm","Did you fill out all the information ?")
    if status>0:
        print("press YES")
        window = Tk()
        window.title("New Window")
        window.geometry("200x200")
        window.mainloop()

def exitProgram():
    #myScreen.destroy()
    Confirm = tkinter.messagebox.askquestion("Confirm ?","Close Progam ?")
    if Confirm == "yes":
        myScreen.destroy()

def ButtonEntry():
    message1 = txt1.get()
    message2 = txt2.get()
    print(message1)
    print(message2)

txt1 = StringVar()
txt2 = StringVar()
myLabel1 = Label(myScreen,text="Username",font=20).place(x=90,y=0)
myLabel2 = Label(myScreen,text="Password",font=20).place(x=90,y=50)
myEntry1 = Entry(myScreen,font=20,textvariable=txt1)
myEntry1.place(x=190,y=0)
myEntry2 = Entry(myScreen,font=20,textvariable=txt2)
myEntry2.place(x=190,y=50)

myButton1 = Button(myScreen,text="Confirm",font=30,command=showConfirm).place(x=90,y=100)

def deleteText():
    myEntry1.delete(0,END)
    myEntry2.delete(0,END)
myButton2 = Button(text="Clear",font=20,command=deleteText).place(x=240,y=100)

myButton3 = Button(text="Exit",font=20,command=exitProgram).place(x=365,y=100)

myScreen.mainloop()