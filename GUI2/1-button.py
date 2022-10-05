from tkinter import *
from tkinter import ttk

GUI = Tk() # นี่คือหน้าต่างหลักของโปรแกรม
GUI.geometry('500x300') #ปรับขนาด
GUI.title('ตัวอย่าง')

B1 = Button(GUI,text='Hello')
B1.pack(pady=10)

# pady=10 คือการทำให้มีระยะห่างแนวบนล่าง 10 พิกเซล


F1 = Frame(GUI)# F1 คือ เฟรม (white board ติดผนัง)
F1.place(x=20,y=20)

B2 = ttk.Button(F1,text='สวัสดี')
B2.pack(ipadx=20,ipady=10)

B3 = ttk.Button(F1,text='บันทึก')
B3.pack(ipadx=20,ipady=10)

GUI.mainloop() # ทำให้โปรแกรมรันได้ตลอดเวลา
