''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#***** ห้ามย่อโค๊ดเด็ดขาดตรงท่อนใส่ [ grid ] มันจะทำให้โปรแกรม error ****#
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 1 บาท = 0.026 EUR ยูโร
# 1 บาท = 3.486 JPY เยน
# 1 บาท = 0.031 USD ดอลล่า
# 1 บาท = 0.023 GBP ปอนด์

#SetUp
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Currency Excahnge")

#Input
money = IntVar()
Label(text="Amount Available",padx=10,font=30).grid(row=0,sticky=W)
et1=Entry(font=30,width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="Please Choose Your Currency")
Label(text="Choose Your Currency",padx=10,font=30).grid(row=1,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=choice)
combo["values"]=("EUR","JPY","USD","GBP")
combo.grid(row=1,column=1)

#Output
Label(text="Result",padx=10,font=30).grid(row=2,sticky=W)
et2=Entry(font=30,width=30)
et2.grid(row=2,column=1)

def calculate():
    amount=money.get()
    currency=choice.get()

    if currency == "EUR":
        et2.delete(0,END)
        result = ((amount*0.026),"EUR(ยูโร)")
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result = ((amount*3.486),"JPY(เยน)")
        et2.insert(0,result)
    elif currency == "USD":
        et2.delete(0,END)
        result = ((amount*0.031),"USD(ดอลล่า)")
        et2.insert(0,result)
    elif currency == "GBP":
        et2.delete(0,END)
        result = ((amount*0.023),"GBP(ปอนด์)")
        et2.insert(0,result)
    else : 
        et2.delete(0,END)
        result = "ไม่พบข้อมูล"
        et2.insert(0,result)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)

Button(text="Calculate",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="Clear",font=30,width=15,command=deleteText).place(x=90,y=100)

root.mainloop()