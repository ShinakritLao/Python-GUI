from tkinter import *
root = Tk()
root.title("Data Entry")

def ButtonEntry():
    message1 = txt1.get()
    message2 = txt2.get()
    message3 = txt3.get()
    Label(text="Keep Data Already").grid(row=4,column=0)
    print(message1)
    print(message2)
    print(message3)
    print("Keep Data Already")
    Label(text=message1).grid()
    Label(text=message2).grid()
    Label(text=message3).grid()

txt1 = StringVar()
txt2 = StringVar()
txt3 = StringVar()

Label(text="FirstName").grid(row=0)
Label(text="LastName").grid(row=1)
Label(text="PhoneNumber").grid(row=2)

et1=Entry(textvariable=txt1)
et1.grid(row=0,column=1)
et1.insert(0,"Shinakrit")


et2=Entry(textvariable=txt2)
et2.grid(row=1,column=1)
et2.insert(0,"Laokittichai")


et3=Entry(textvariable=txt3)
et3.grid(row=2,column=1)
et3.insert(0,"081-869-5464")

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)

btn1 = Button(text="Clear",command=deleteText).grid(row=3,column=0)
btn2 = Button(text="Send",command=ButtonEntry).grid(row=3,column=1)

root.mainloop()