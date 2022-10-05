#entry-label.py

from tkinter import *
from tkinter import ttk

GUI = Tk() # นี่คือหน้าต่างหลักของโปรแกรม
GUI.geometry('500x300') #ปรับขนาด
GUI.title('ตัวอย่าง Entry - Label')

FONT1 = ('Angsana New',15)
FONT2 = ('Angsana New',20,'bold')

# v_expense ใช้สำหรับเก็บค่าที่ user พิมพ์
v_expense = StringVar()

# E1 คือช่องกรอกข้อมูล
L = ttk.Label(GUI,text='กรุณากรอกรายจ่าย').pack() #หัวข้อบนช่องกรอก
E1 = ttk.Entry(GUI,textvariable=v_expense, font=FONT1, width=30)
E1.pack(pady=10)

# v_expense ใช้สำหรับเก็บค่าที่ user พิมพ์
v_price = StringVar()

# E1 คือช่องกรอกข้อมูล
L = ttk.Label(GUI,text='ค่าใช้จ่าย (บาท)').pack() #หัวข้อบนช่องกรอก
E2 = ttk.Entry(GUI,textvariable=v_price, font=FONT1, width=30)
E2.pack(pady=10)


# SaveExpense คือฟังชั่นเมื่อมีการกดปุ่ม ฟังชั่นนี้จะทำงาน
def SaveExpense(event=None):
    exp = v_expense.get()
    pc = float(v_price.get()) # แปลงข้อความเป็นจุดทศนิยม
    # ข้อความเป็นตัวเลขใช้ int() , ข้อความเป็นจุดทศนิยม float() , ตัวเลขหรือจุดทุศนิยมเป็นข้อความ str()
    print('รายการ: ',exp) # v_expense.get() คือการดึงค่ามาใช้งาน
    #v_result.set('คุณกำลังบันทึกรายการ: ' + exp + ' ราคา: '+ v_price.get() +' บาท')
    v_result.set(f'กำลังบันทึกรายการ: {exp} ราคา: {pc:,.2f} บาท')

    #reset ตัวแปร
    v_expense.set('')
    v_price.set('')
    #ทำให้ cursor วิ่งไปหาช่องกรอกตัวแรก
    E1.focus()
    

E2.bind('<Return>',SaveExpense) #หากใช้ bind ต้องใส่ event=None ในฟังชั่นด้วย

# B1 คือปุ่มสำหรับกดบันทึก
B1 = ttk.Button(GUI,text='บันทึก',command=SaveExpense)
B1.pack()

#######LABEL########
v_result = StringVar()
R1 = ttk.Label(GUI, textvariable= v_result, font=FONT2, foreground='green') # R1 = Label(fg='green')
R1.pack(pady=20)


GUI.mainloop() # ทำให้โปรแกรมรันได้ตลอดเวลา
