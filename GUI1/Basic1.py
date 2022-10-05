
from tkinter import *
from tkinter import ttk #ใช้เปลี่ยน texture ปุ่ม ใส่หน้า Button
#myButton1 = ttk.Button(myScreen,text = 'Hello').pack()
from tkinter.colorchooser import *
from tkinter.filedialog import *
import tkinter.messagebox

#หน้าจอที่ 1
myScreen = Tk()
myScreen.title("My GUI")
myScreen.geometry("650x750")

#หน้าจอ 2
'''อยู่ในCommand'''

#ส้ราง Menu
myMenu = Menu()
myScreen.config(menu=myMenu)
''''''
#Commandเมนูย่อย
def showWindow():
    window = Tk()
    window.title("New Window")
    window.geometry("200x200")
    window.mainloop()
''''''
#Commandปิดหน้าจอ 1
def exitProgram():
    #myScreen.destroy()
    Confirm = tkinter.messagebox.askquestion("Confirm ?","Close Progam ?")
    if Confirm == "yes":
        myScreen.destroy()
''''''
def aboutProgram():
    tkinter.messagebox.showinfo("ผู้พัฒนาโปรแกรม" , "SHINYSHINE")
''''''
#เพิ่ม Menu ย่อย
myItem1 = Menu()
myItem2 = Menu()
myItem3 = Menu()
myItem4 = Menu()
myItem5 = Menu()
''''''
myItem1.add_command(label = "New",command = showWindow)
myItem1.add_command(label = "Open")
myItem1.add_command(label = "Save")
myItem1.add_command(label = "About",command = aboutProgram)
myItem1.add_command(label = "Exit",command = exitProgram)
''''''
myItem2.add_command(label = "Item 2.1")
myItem2.add_command(label = "Item 2.2")
myItem2.add_command(label = "Item 2.3")
''''''
myItem3.add_command(label = "Item 3.1")
myItem3.add_command(label = "Item 3.2")
myItem3.add_command(label = "Item 3.3")
''''''
myItem4.add_command(label = "Item 4.1")
myItem4.add_command(label = "Item 4.2")
myItem4.add_command(label = "Item 4.3")
''''''
myItem5.add_command(label = "Item 5.1")
myItem5.add_command(label = "Item 5.2")
myItem5.add_command(label = "Item 5.3")
''''''
#เพิ่ม Menu หลัก
myMenu.add_cascade(label="File",menu=myItem1)
myMenu.add_cascade(label="Edit",menu=myItem2)
myMenu.add_cascade(label="View",menu=myItem3)
myMenu.add_cascade(label="Go",menu=myItem4)
myMenu.add_cascade(label="Run",menu=myItem5)

#Commandใช้ปุ่ม
def showMessage():
    print("Show Messsage")
    Label(myScreen,text="Show Message",fg="black",bg="gray",font=30).pack()

#Commandปุ่มและกล่องข้อความ
def ButtonEntry():
    message = txt.get() #ได้เหมือนกับที่ป้อน
    print(message)
    Label(myScreen,text=message,fg="white",bg="grey",font=20).pack()

#Command เปิดหน้าจอ 2
def OpenWindow():
    myWindow = Tk()
    myWindow.title("รายงานผลการทำงาน")
    myWindow.geometry("300x300")
    myWindow.mainloop()



"""fg=สีตัวอักษร font=ขนาดข้อความ bg=สีพื้นหลัง""" """pack ใช้ร่วมกับ grid ไม่ได้"""
#ใส่ข้อความในหน้าจอ  .pack()
myLabel1 = Label(myScreen,text="Hello World",fg="brown",bg="green",font=30).pack(ipadx=50,ipady=50) #ipadx,ipady คือ ขนาดกล่อง
myLabel2 = Label(myScreen,text="Shinakrit Laokittichai",fg="white",bg="blue",font=20).pack()
#ใส่ข้อความในหน้าจอ  .place(x=50,y=50)
myLabel3 = Label(myScreen,text="SHINNYSHINE",fg="black",bg="white",font=20).place(x=20,y=20)
#ใส่ข้อความในหน้าจอ  .grid(row=5,column=5)
'''
myLabel4 = Label(myScreen,text="SHIN",fg="black",bg="white",font=20).grid(row=0,column=0)
myLabel5 = Label(myScreen,text="SHINS",fg="black",bg="white",font=20).grid(row=1,column=1)
'''

#สร้างปุ่ม
myButton1 = Button(myScreen,text="LEFT",fg="white",bg="black",font=30).pack(side=LEFT)
myButton2 = Button(myScreen,text="RIGHT",fg="white",bg="black",font=30).pack(side=RIGHT)
myButton3 = Button(myScreen,text="Show",fg="white",bg="black",font=30,command=showMessage).pack()

#กล่องข้อความ
txt = StringVar()
myText = Entry(myScreen,textvariable=txt).pack()
myButton4 = Button(myScreen,text="Send",fg="white",bg="black",font=30,command=ButtonEntry).pack()

#เปิดหน้าจอ 2
myButton5 = Button(myScreen,text="Open",fg="white",bg="black",font=30,command=OpenWindow).pack()

#Commandหน้าต่างเลือกสี
def selectColor():
    color = askcolor()
    myLabel6 = Label(myScreen,text="Your Color",bg=color[1],font=12).pack()
    myLabel7 = Label(myScreen,text=color,bg=color[1],font=12).pack()
    print(color)
myButton6 = Button(myScreen,text="Choose Color",fg="white",bg="black",font=30,command=selectColor).pack()

#Commandหน้าต่างเลือกไฟล์   +   อ่านเนื้อหาไฟล์("รอแก้ไข")***
def selectFile():
    fileOpen = askopenfile()
    #fileContent = open(fileOpen)
    myLabel8 = Label(myScreen,text=fileOpen,font=12).pack()
    #myLabel9 = Label(myScreen,text=fileContent.read(),font=12).pack()
myButton7 = Button(myScreen,text="Choose File",fg="white",bg="black",font=30,command=selectFile).pack()

#Commandเลือกตัวเลือก
def showChoice():
    choice=comLanguage.get()
    if choice == 1:
        tkinter.messagebox.showinfo("Notification","You Choose Python")
    elif choice == 2:
        tkinter.messagebox.showinfo("Notification","You Choose C++")
    elif choice == 3:
        tkinter.messagebox.showinfo("Notification","You Choose JAVA")
    elif choice == 4:
        tkinter.messagebox.showinfo("Notification","You Choose PHP")
#เพิ่มตัวเลือกในโปรแกรม
comLanguage = IntVar()
#เซ็ตเริ่มต้น comLanguage.set(1)
Radiobutton(text="Python",font=10,variable=comLanguage,value=1,command=showChoice).pack()
Radiobutton(text="C++",font=10,variable=comLanguage,value=2,command=showChoice).pack()
Radiobutton(text="JAVA",font=10,variable=comLanguage,value=3,command=showChoice).pack()
Radiobutton(text="PHP",font=10,variable=comLanguage,value=4,command=showChoice).pack()

#Commandเช็คคำตอบ
def sendChoice():
    choice1 = animal1.get()
    choice2 = animal2.get()
    choice3 = animal3.get()
    choice4 = animal4.get()
    if choice1 == 1:
        Label(myScreen,text="You Choose Dog",font=10).pack(anchor=W)
    if choice2 == 1:
        Label(myScreen,text="You Choose Cat",font=10).pack(anchor=W)
    if choice3 == 1:
        Label(myScreen,text="You Choose Bird",font=10).pack(anchor=W)
    if choice4 == 1:
        Label(myScreen,text="You Choose Fish",font=10).pack(anchor=W)
    print(animal1.get(),animal2.get(),animal3.get(),animal4.get())
    # 0 = ไม่ไได้เลือก   1 = เลือกตัวเลือก
#เช็คปุ่มMultipleChoice
animal1 =IntVar()
Checkbutton(text="Dog",font=10,variable=animal1).pack(anchor=W)
animal2 =IntVar()
Checkbutton(text="Cat",font=10,variable=animal2).pack(anchor=W)
animal3 =IntVar()
Checkbutton(text="Bird",font=10,variable=animal3).pack(anchor=W)
animal4 =IntVar()
Checkbutton(text="Fish",font=10,variable=animal4).pack(anchor=W)
myButton8 = Button(text="แสดงตัวเลือก",font=10,command=sendChoice).pack(anchor=W)

myScreen.mainloop()