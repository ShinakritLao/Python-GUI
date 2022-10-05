from tkinter import *   #เรียก GUI    (ต้องมี)
from tkinter import ttk #เรียก Format (ไม่มีก็ได้) ถ้าไม่มีต้องลบ ttk.
import tkinter.messagebox #เรียก messagebox popup เด้งขึ้นมา
#หรือจะต่อแบบนี้ก็ได้ from tkinter import ttk, messagebox
#ถ้าต่อกันลบ tkinter. ได้เลย
from datetime import datetime #เรียกการใช้เวลา
import csv  #เรียกเพื่อบันทึกข้อมูล

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')
GUI.geometry('600x600')

menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

def About():
	tkinter.messagebox.showinfo('About','สวัสดีค่ะ นี่เป็นโปรแกรมบันทึกข้อมูล\nสนใจบริจาคให้เรามั้ยคะ? ขอแค่ 1 BTC ก็พอแล้ว\nBTC Address : ยังไม่ได้สมัคร')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

def Donate():
	tkinter.messagebox.showinfo('Daonte','dogecoin network : ยังไม่ได้สมัคร')
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='Donate',command=Donate)

Tab = ttk.Notebook(GUI) #import จาก ttk
Tab1 = Frame(Tab) #สร้างแท๊ปข้างบน
Tab2 = Frame(Tab) #สร้างแท๊ปข้างบน
Tab.pack(fill=BOTH,expand=1) #ขยายให้เห็น

Icon_Tab1 = PhotoImage(file='Tab1.png') #นำรูปภาพมาใช้งาน
Icon_Tab2 = PhotoImage(file='Tab2.png') #นำรูปภาพมาใช้งาน
#ถ้ารูปภาพไม่ได้ขนาดย่อได้ใช้คำส่งต่อท้าย .subsample(เป็นตัวเลข กี่เท่า)

Tab.add(Tab1, text=f'{"เพิ่มค่าใช้จ่าย":^{30}}',image=Icon_Tab1,compound='top')    #ตั้งชื่อแท๊ปใส่รูป
Tab.add(Tab2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=Icon_Tab2,compound='top')  #ตั้งชื่อแท๊ปใส่รูป
#f'{"ข้อความ":^{ขนาดข้อความ}}' คือ เซ็ตข้อความให้สวยงาม
#image=ชื่อที่ตั้งเป็นหัวข้อ,compound='ทิศ (left right top bottom)' เพื่อความสงยงามไม่จำเป็นต้องมี

Frame1 = Frame(Tab1) #คล้ายๆกระดานซ้อนกระดาน(GUI) ยัดไว้ในTab1(Tab1)
Frame1.pack(pady=20) #เว้นด้านบน #.place(x=155,y=50) #วางไว้บน GUI ตามตำแหน่ง

Day = {'Mon':'จันทร์',
	   'Tue':'อังคาร',
	   'Wed':'พุธ',
	   'Thu':'พฤหัสบดี',
	   'Fri':'ศุกร์',
	   'Sat':'เสาร์',
	   'Sun':'อาทิตย์'}

#[\/\/\/\/\/\/\/\/\/\/\ - TAB1 - /\/\/\/\/\/\/\/\/\/\/]#

def Save(event=None): #สร้างฟังก์ชั่น รอเรียกใช้
	Expense = txt_Expense.get()   #ดึงค่า ตัวแปรtxt จากช่อง Entry1
	Price = txt_Price.get()       #ดึงค่า ตัวแปรtxt จากช่อง Entry2
	Quantity = txt_Quantity.get() #ดึงค่า ตัวแปรtxt จากช่อง Entry3

	if Expense == '': #เช็คว่าใส่ช่องรายการค่าใช้จ่ายยัง
		print('No Data of Expense')
		tkinter.messagebox.showerror("Error","กรุณากรอกรายการค่าใช้จ่าย !!")
		#มี messagebox เด้งขึ้นมา มี showerror showwarning showinfo
		return
	elif Price == '': #เช็คว่าใส่ช่องราคา
		print('No Data of Price')
		cccmessagebox.showerror("Error","กรุณากรอกราคา !!")
		#มี messagebox เด้งขึ้นมา มี showerror showwarning showinfo
		return
	elif Quantity == '': #เช็คว่าใส่ช่องจำนวน
		print('No Data of Quantity')
		tkinter.messagebox.showerror("Error","กรุณากรอกจำนวน !!")
		#มี messagebox เด้งขึ้นมา มี showerror showwarning showinfo
		return

	try: #เอาไว้เช็คว่าเกิดข้อผิดพลาดอะไรหรือเปล่า
		Total = float(Price) * float(Quantity)

		print('รายการ: {}  ราคา: {}'.format(Expense,Price))
		#ปริ้้นข้อมูลจาก Entry1,2,3
		print('จำนวน : {}  รวมทั้งหมด: {} บาท'.format(Quantity,Total))
		#ปริ้นเงินทั้งหมด

		#บันทึกข้อมูลเวลา ต้อง from datetime import datetime
		#.strftime('พิ่มเติมข้อมูลวันเวลา ลองเปิดกูเกิล strftime') คือ StringFormatTime
		Today = datetime.now().strftime('%a')
		print(Today)
		Date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		Date = Day[Today] + '-' + Date
		print(Date)

		#บันทึกข้อมูล csv ต้อง import csv
		#จะเปิดไฟล์ที่เก็บข้อมูลจะต้อง คลิ๊กขวา กด Edit
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
		#สร้างฟังก์ชั่นสำหรับการเชียนข้อมูล
			#with        คือ สั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			#'a'         คืิอ การบันทึกเรื่อยๆ เพิ่มข้อมูลจากข้อมูลเก่า
			#'w'         คือ การบันทึกข้อมูลเดียว พอบันทึกเพิ่มจะลบของเก่า
			#utf-8       คือ ทำให้บันทึกภาษาไทยได้
			#newline=''  คือทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) #สร้างตัวแปรเก็บข้อมูลจากการเขียนข้อมูล
			data = [Date,Expense,Price,Quantity,Total] #เรียงลำดับข้อมูลที่เก็บ
			fw.writerow(data)

		TextResult = '[-----------------ผลลัพธ์-----------------]\n'
		TextResult = TextResult + 'รายการ : {} ราคา : {}\n'.format(Expense,Price)
		TextResult = TextResult + 'จำนวน : {} รวมทั้งหมด : {}\n'.format(Quantity,Total)
		TextResult = TextResult + Today + '-' + Date
		#เตรียมข้อความทังหมด
		TitleResult.set(TextResult) #เซ็ตให้ปริ้นข้อความ

		#Clear ข้อมูลเก่า
		txt_Expense.set('')
		txt_Price.set('')
		txt_Quantity.set('')

		#ทำให้เคอเซอร์กลับไปที่ช่อง Entry1
		Entry1.focus()
		update_table()


	except Exception as e: #ถ้า error จะดำเนินตาม except
	#Exception คือ การเช็คว่าทำอะไรผิดเลย error // as e แทน e
		print('ERROR : ',e)
		tkinter.messagebox.showerror("Error","กรุณาใส่ข้อมูลให้ถูกต้อง !!")
		#มี messagebox เด้งขึ้นมา มี showerror showwarning showinfo

		#Clear ข้อมูลเก่า
		txt_Expense.set('')
		txt_Price.set('')
		txt_Quantity.set('')

#ทำให้สามารถกด enter ได้ [enter = Return]
GUI.bind('<Return>',Save) #สั่งถ้ากดปุ่ม enter แล้วเริ่มฟังก์ชัน Save ข้างบน
#ต้องเพิ่มใน def Save(event=None)
#ถ้าไม่มีบรรทัดนี้ไม่ต้องใส่ (event=None)

#-------------Main-Icon-------------#
Icon_Main = PhotoImage(file='MainIcon.png') #นำรูปภาพมาใช้งาน
#ถ้ารูปภาพไม่ได้ขนาดย่อได้ใช้คำส่งต่อท้าย .subsample(เป็นตัวเลข กี่เท่า)
Mainicon = Label(Frame1,image=Icon_Main) #ไว้ใน Frame1
Mainicon.pack()
#-----------------------------------#

#---------------Text1---------------#
Font1 = (None,20) #None สามารถเปลี่ยนเป็น 'Angsana New'
#ฟอนต์
Label1 = ttk.Label(Frame1,text='รายการค่าใช้จ่าย',font=Font1).pack()
#ตัวอักษร
txt_Expense = StringVar() #StringVar() เป็นตัวแปรพอเศษสำหรับเก็บข้อมูลใน GUI
Entry1 = ttk.Entry(Frame1,textvariable=txt_Expense,font=Font1)
Entry1.pack()
#ช่องเติม
#-----------------------------------#

#---------------Text2---------------#
Font2 = (None,20) #None สามารถเปลี่ยนเป็น 'Angsana New'
#ฟอนต์
Label2 = ttk.Label(Frame1,text='ราคา (บาท)',font=Font2).pack()
#ตัวอักษร
txt_Price = StringVar() #StringVar() เป็นตัวแปรพอเศษสำหรับเก็บข้อมูลใน GUI
Entry2 = ttk.Entry(Frame1,textvariable=txt_Price,font=Font2)
Entry2.pack()
#ช่องเติม
#-----------------------------------#

#---------------Text3---------------#
Font3 = (None,20) #None สามารถเปลี่ยนเป็น 'Angsana New'
#ฟอนต์
Label3 = ttk.Label(Frame1,text='จำนวน (ชิ้น)',font=Font3).pack()
#ตัวอักษร
txt_Quantity = StringVar() #StringVar() เป็นตัวแปรพอเศษสำหรับเก็บข้อมูลใน GUI
Entry3 = ttk.Entry(Frame1,textvariable=txt_Quantity,font=Font3)
Entry3.pack()
#ช่องเติม
#-----------------------------------#

#--------------Button1--------------#
Icon_But1 = PhotoImage(file='Save.png') #นำรูปภาพมาใช้งาน
#ถ้ารูปภาพไม่ได้ขนาดย่อได้ใช้คำส่งต่อท้าย .subsample(เป็นตัวเลข กี่เท่า)

Button1 = ttk.Button(Frame1,text='   Save',image=Icon_But1,compound='left',command=Save)
#ปุ่มที่เชื่อมกับฟังก์ชั่น Save  ตรงtextเพิ่มแบบเคาะแทนก็ได้
#f'{"ข้อความ":^{ขนาดข้อความ}}' คือ เซ็ตข้อความให้สวยงาม
#image=ชื่อที่ตั้งเป็นหัวข้อ,compound='ทิศ (left right top bottom)' เพื่อความสวยงามไม่จำเป็นต้องมี
Button1.pack(ipadx=20,ipady=10) #ความกว้างยาวปุ่ม
#-----------------------------------#

#---------------Result--------------#
Font4 = (None,20) #None สามารถเปลี่ยนเป็น 'Angsana New'
TitleResult = StringVar()
TitleResult.set('[-----------------ผลลัพธ์-----------------]')
Result = ttk.Label(Frame1,textvariable=TitleResult,font=Font4,foreground='green')
Result.pack(pady=20) #เว้นด้านบน
#-----------------------------------#

#[\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/]#

#[\/\/\/\/\/\/\/\/\/\/\ - TAB2 - /\/\/\/\/\/\/\/\/\/\/]#

def Read_csv(): #สร้างฟังก์ชั่นเพื่ออ่านค่า csv
	with open('savedata.csv',newline='',encoding='utf-8') as f:
		#with        คือ สั่งเปิดไฟล์แล้วปิดอัตโนมัติ
		#utf-8       คือ ทำให้บันทึกภาษาไทยได้
		#newline=''  คือทำให้ข้อมูลไม่มีบรรทัดว่าง
		fr = csv.reader(f) #สร้างฟังก์ชั่นสำหรับการเชียนข้อมูล
		data = list(fr) #สร้าง list ให้อ่านค่าได้
	return data

#---------------Table---------------#
Label4 = ttk.Label(Tab2,text='ตารางแสดงผลลัพท์ทั้งหมด',font=Font1).pack(pady=20)
Header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(Tab2,columns=Header,show='headings',height=20)
resulttable.pack()

for h in Header: #เรียก h เก็บ ตัวแปร Header
	resulttable.heading(h,text=h) #เอาเข้า header ตาราง
Headerwidth = [150,170,80,80,80] #ขนาดของ Header
#วิธี Manual เปลี่ยนชื่อด้านหลังได้ แต่ไม่จำเป็นเปลี่ยนหัวข้อเลยก็ได้
#resulttable.heading('วัน-เวลา',text='วัน-เวลา',width=150)
#resulttable.heading('รายการ',text='รายการ',width=170)
#resulttable.heading('ค่าใช้จ่าย',text='ค่าใช้จ่าย',width=80)
#resulttable.heading('จำนวน',text='จำนวน',width=80)
#resulttable.heading('รวม',text='รวม',width=80)

for h,w in zip(Header,Headerwidth):
	resulttable.column(h,width=w)

def update_table():
	resulttable.delete(*resulttable.get_children())
	#for c in resultable.get_children():
	#resultable.delete(c)
	data = Read_csv()
	print(data)
	for d in data:
		resulttable.insert('',0,value=d)

update_table()
print('GET CHILD : ',resulttable.get_children())


#-----------------------------------#

#[\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/]#

GUI.bind('<Tab>',lambda x: Entry1.focus()) #กด Tab เพื่อเปลี่ยนบรรทัด
GUI.bind('<Tab>',lambda x: Entry2.focus()) #กด Tab เพื่อเปลี่ยนบรรทัด
GUI.bind('<Tab>',lambda x: Entry3.focus()) #กด Tab เพื่อเปลี่ยนบรรทัด

GUI.mainloop()
