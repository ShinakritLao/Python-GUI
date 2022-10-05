''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#***** ห้ามย่อโค๊ดเด็ดขาดตรงท่อนใส่ [ grid ] มันจะทำให้โปรแกรม error ****#
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#SetUp
from tkinter import *
root = Tk()
root.title("Calculator")

content = ""
txt_input = StringVar(value="0")

#Button
def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

#Clear
def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = ""

#Clear
def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")

#Display
display = Entry(font=('arial',32,'bold'),fg="white",bg="green",textvariable=txt_input,justify="right")
display.grid(columnspan=4)

#Row 1 : ( ) = =
btnBanketLeft = Button(fg="Brown",font=('arial',30,'bold'),text="(",command=lambda:btn("("),padx=35,pady=15).grid(row=1,column=0)
btnBanketRight = Button(fg="Brown",font=('arial',30,'bold'),text=")",command=lambda:btn(")"),padx=35,pady=15).grid(row=1,column=1)
btnEqual = Button(fg="Red",bg="Gray",font=('arial',30,'bold'),text="=",command=equal,padx=93,pady=15).grid(row=1,column=2,columnspan=2)

#Row 2 : 7 8 9 C
btn7 = Button(fg="black",font=('arial',30,'bold'),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=2,column=0)
btn8 = Button(fg="black",font=('arial',30,'bold'),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=2,column=1)
btn9 = Button(fg="black",font=('arial',30,'bold'),text="9",command=lambda:btn(9),padx=30,pady=15).grid(row=2,column=2)
btnC = Button(fg="Red",bg="Gray",font=('arial',30,'bold'),text="C",command=clear,padx=32,pady=15).grid(row=2,column=3)

#Row 3 : 4 5 6 +
btn4 = Button(fg="black",font=('arial',30,'bold'),text="4",command=lambda:btn(4),padx=30,pady=15).grid(row=3,column=0)
btn5 = Button(fg="black",font=('arial',30,'bold'),text="5",command=lambda:btn(5),padx=30,pady=15).grid(row=3,column=1)
btn6 = Button(fg="black",font=('arial',30,'bold'),text="6",command=lambda:btn(6),padx=30,pady=15).grid(row=3,column=2)
btnPlus = Button(fg="Blue",font=('arial',30,'bold'),text="+",command=lambda:btn("+"),padx=35,pady=15).grid(row=3,column=3)

#Row 4 : 1 2 3  -
btn1 = Button(fg="black",font=('arial',30,'bold'),text="1",command=lambda:btn(1),padx=30,pady=15).grid(row=4,column=0)
btn2 = Button(fg="black",font=('arial',30,'bold'),text="2",command=lambda:btn(2),padx=30,pady=15).grid(row=4,column=1)
btn3 = Button(fg="black",font=('arial',30,'bold'),text="3",command=lambda:btn(3),padx=30,pady=15).grid(row=4,column=2)
btnMinus = Button(fg="Blue",font=('arial',30,'bold'),text="-",command=lambda:btn("-"),padx=40,pady=15).grid(row=4,column=3)

#Row 5 : . 0 / x
btnDot = Button(fg="Blue",font=('arial',30,'bold'),text=".",command=lambda:btn("."),padx=35,pady=15).grid(row=5,column=0)
btn0 = Button(fg="black",font=('arial',30,'bold'),text="0",command=lambda:btn(0),padx=30,pady=15).grid(row=5,column=1)
btnDivision = Button(fg="Blue",font=('arial',30,'bold'),text="/",command=lambda:btn("/"),padx=35,pady=15).grid(row=5,column=2)
btnMultiple = Button(fg="Blue",font=('arial',30,'bold'),text="x",command=lambda:btn("*"),padx=35,pady=15).grid(row=5,column=3)

root.mainloop()