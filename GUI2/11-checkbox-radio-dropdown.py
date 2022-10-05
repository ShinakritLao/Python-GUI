#11-checkbox-radio-dropdown.py

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าต่างหลักของโปรแกรม
GUI.title('ตัวอย่าง')
w = 500
h = 300
ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws,hs)
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #ปรับขนาด
#GUI.state('zoomed')

###################RADIO BUTTON######################
F1 = Frame(GUI)
F1.pack(pady=10)

v_radio = StringVar() #เก็บค่าจากการเลือก

RB1 = ttk.Radiobutton(F1,text='Pop up',variable=v_radio, value='popup')
RB2 = ttk.Radiobutton(F1,text='print',variable=v_radio, value='print')
RB1.grid(row=0,column=0)
RB2.grid(row=0,column=1)
RB1.invoke() #ทำให้ RB1 เป็นค่า default

def Run():
	v = v_radio.get() #ดึงค่าจากตัวแปรที่เก็บค่าของ radio
	print(v) 

	if v == 'popup':
		messagebox.showinfo('Popup','คุณกำลังเลือก popup') # โชว์ข้อความแจ้งให้ทราบ
		#messagebox.showwarning('Popup','คุณกำลังเลือก popup') #โชว์ข้อความแจ้งเตือน
		#messagebox.showerror('Popup','คุณกำลังเลือก popup') #โชว์ข้อความมีปัญหา
	else:
		print('คุณไม่ได้เลือก popup คุณเลือก print')


B1 = ttk.Button(GUI,text='Run',command=Run)
B1.pack()

###################CHECK BUTTON######################
F2 = Frame(GUI)
F2.pack(pady=10)

c1 = StringVar()
c1.set('ไม่เอาข้าว') #set ค่า default
c2 = StringVar()
c2.set('ไม่ใส่ปลา')
c3 = StringVar()
c3.set('น้ำดื่มมีแล้ว')

C1 = Checkbutton(F2,text='ข้าว',onvalue='ข้าว',offvalue='ไม่เอาข้าว',variable=c1)
C1.grid(row=0,column=1)
C1.invoke()

C2 = ttk.Checkbutton(F2,text='ปลา',onvalue='ปลา',offvalue='ไม่ใส่ปลา',variable=c2)
C2.grid(row=0,column=2)

C3 = Checkbutton(F2,text='น้ำดื่ม',onvalue='น้ำดื่ม',offvalue='น้ำดื่มมีแล้ว',variable=c3)
C3.grid(row=0,column=3)

def SelectFood():
	C1.deselect()

B2 = ttk.Button(GUI,text='Select Food',command=SelectFood)
B2.pack()
###################COMBO BOX (Dropdown) ######################
cblist = ['บัตรเครดิต','เงินสด','โอน']

CB1 = ttk.Combobox(GUI,values=cblist)
CB1.set('เงินสด')
CB1.place(x=20,y=200)

def Dropdown():
	print(CB1.get())

B3 = ttk.Button(GUI,text='Dropdown',command=Dropdown)
B3.place(x=200,y=200)

GUI.mainloop() # ทำให้โปรแกรมรันได้ตลอดเวลา
