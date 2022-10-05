#GUIExpense.py

from tkinter import *
from tkinter import ttk
#########CSV##########
import csv

#Comma-separated values: CSV

###########WritetoCSV - for Expense #############
def WritetoCSV(ep):
	with open('allexpense.csv','a',newline='',encoding='utf-8') as file:
		# 'a' = append (เพิ่มได้เรื่อยๆ) , 'w' = replace (ทับไฟล์เดิม)
		fw = csv.writer(file) # fw คือ file writer
		# ep = ['ไก่',300]
		fw.writerow(ep)

	print('Done!')

def ReadCSV():
	with open('allexpense.csv',newline='',encoding='utf-8') as file:
		#fr = file reader
		fr = csv.reader(file)
		#print(list(fr))
		data = list(fr)
	return data

###########WritetoCSV2 - for Income #############
def WritetoCSV2(ep):
	with open('allincome.csv','a',newline='',encoding='utf-8') as file:
		# 'a' = append (เพิ่มได้เรื่อยๆ) , 'w' = replace (ทับไฟล์เดิม)
		fw = csv.writer(file) # fw คือ file writer
		# ep = ['ไก่',300]
		fw.writerow(ep)

	print('Done!')

def ReadCSV2():
	with open('allincome.csv',newline='',encoding='utf-8') as file:
		#fr = file reader
		fr = csv.reader(file)
		#print(list(fr))
		data = list(fr)
	return data

########MAIN GUI########
GUI = Tk() # นี่คือหน้าต่างหลักของโปรแกรม
GUI.title('GUI Expense')



w = 700
h = 700

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #ปรับขนาด
GUI.iconbitmap('wallet.ico')
#GUI.state('zoomed')

########FONT#########
s = ttk.Style()
s.configure('my.TButton',font=('TH Sarabun New',15,'bold'))



menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Exit - (F4)',command=GUI.quit)
#command= lambda: GUI.destroy()
GUI.bind('<F4>',lambda x: GUI.destroy())

## helpmenu
import webbrowser

def About():
	url = 'https://www.youtube.com/watch?v=chY9p-XLHHk'
	webbrowser.open(url)

from tkinter import messagebox as msb

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About', command=About)
helpmenu.add_command(label='Donate',command=lambda: msb.showinfo('Donate','เลขบัญชี: 226 0 337 742\nธนาคารกรุงเทพ (บัวหลวง)'))
#command=lambda: msb.showinfo('Donate','เลขบัญชี: 226 0 337 742\nธนาคารบัวหลวง')


from tkinter.ttk import Notebook

Tab = Notebook(GUI)
Tab.pack(fill=BOTH, expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

icon_expense = PhotoImage(file='cart.png')
icon_income = PhotoImage(file='money.png')
icon_dashboard = PhotoImage(file='dashboard.png')

Tab.add(T1,text='รายจ่าย',image=icon_expense,compound='top')
Tab.add(T2,text='รายรับ',image=icon_income,compound='top')
Tab.add(T3,text='สรุปผล',image=icon_dashboard,compound='top')


#################################################

G = Canvas(T3,width=400,height=300)
G.place(x=200,y=230)


def UpdateGraph(expense=100,income=200):

	if income >= expense:
		ep = int((expense / income) * 300)
		ic = 298
	else:
		ic = int((income / expense) * 300)
		ep = 298

	start_y = 300
	total = 300

	print('income', ic)
	print('expense', ep)
	hb1 = ep
	hb2 = ic
	hb3 = hb2 - hb1

	G.delete(ALL)

	b1 = G.create_rectangle(50,total - hb1,100,start_y,fill='orange')
	b2 = G.create_rectangle(150,total - hb2,200,start_y,fill='green')
	b3 = G.create_rectangle(250,total - hb3,300,start_y,fill='blue')

L = ttk.Label(T3,text='รายจ่าย').place(x=250,y=540)
L = ttk.Label(T3,text='รายรับ').place(x=350,y=540)
L = ttk.Label(T3,text='คงเหลือ').place(x=450,y=540)



####################Expense######################

FONT1 = ('Angsana New',15)
FONT2 = ('Angsana New',20,'bold')
FONT3 = ('Angsana New',30,'bold')

# v_expense ใช้สำหรับเก็บค่าที่ user พิมพ์
v_expense = StringVar()

# E1 คือช่องกรอกข้อมูล
L = ttk.Label(T1,text='กรุณากรอกรายจ่าย').pack() #หัวข้อบนช่องกรอก
E1 = ttk.Entry(T1,textvariable=v_expense, font=FONT1, width=30)
E1.pack(pady=10)

# v_expense ใช้สำหรับเก็บค่าที่ user พิมพ์
v_price = StringVar()

# E1 คือช่องกรอกข้อมูล
L = ttk.Label(T1,text='ค่าใช้จ่าย (บาท)').pack() #หัวข้อบนช่องกรอก
E2 = ttk.Entry(T1,textvariable=v_price, font=FONT1, width=30)
E2.pack(pady=10)


# SaveExpense คือฟังชั่นเมื่อมีการกดปุ่ม ฟังชั่นนี้จะทำงาน
from datetime import datetime #เวลา

def SaveExpense(event=None):
	exp = v_expense.get()
	pc = float(v_price.get()) # แปลงข้อความเป็นจุดทศนิยม
	# ข้อความเป็นตัวเลขใช้ int() , ข้อความเป็นจุดทศนิยม float() , ตัวเลขหรือจุดทุศนิยมเป็นข้อความ str()
	print('รายการ: ',exp) # v_expense.get() คือการดึงค่ามาใช้งาน
	#v_result.set('คุณกำลังบันทึกรายการ: ' + exp + ' ราคา: '+ v_price.get() +' บาท')
	v_result.set(f'กำลังบันทึกรายการ: {exp} ราคา: {pc:,.2f} บาท')

	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	data = [dt,exp,pc] #จัดเรียงข้อมูลก่อนเซฟลง csv
	WritetoCSV(data) #เรียกฟังชั่นการบันทึกข้อมูล

	#reset ตัวแปร
	v_expense.set('')
	v_price.set('')
	#ทำให้ cursor วิ่งไปหาช่องกรอกตัวแรก
	E1.focus()
	update_table() #อัพเดตตารางทุกครั้งที่มีการเพิ่มรายการใหม่
	

E2.bind('<Return>',SaveExpense) #หากใช้ bind ต้องใส่ event=None ในฟังชั่นด้วย

# B1 คือปุ่มสำหรับกดบันทึก
B1 = ttk.Button(T1,text='บันทึก',command=SaveExpense, style='my.TButton')
B1.pack(ipadx=20,ipady=10)

#######LABEL########
v_result = StringVar()
R1 = ttk.Label(T1, textvariable= v_result, font=FONT2, foreground='green') # R1 = Label(fg='green')
R1.pack(pady=20)

########Expense Button##########

expenselist = {'rice':{'name':'ข้าว','price':20},
			   'coffee':{'name':'กาแฟ','price':25},
			   'taxi':{'name':'ค่าแท็กซี่','price':35}}

###########FUNCTION########
def Expense(keyword):
	price = expenselist[keyword]['price']
	print('ค่าใช้จ่าย: ' + expenselist[keyword]['name'])
	print('ราคา: ',price)

	ep = expenselist[keyword]['name']
	
	v_expense.set(ep)
	v_price.set(price)

###########ROW1############

F1 = Frame(T1)# F1 คือ เฟรม (white board ติดผนัง)
F1.pack()

B1 = ttk.Button(F1,text='ข้าว',command=lambda x='rice': Expense(x), style='my.TButton')
B1.grid(row=0,column=0,ipadx=20,ipady=10,padx=5)
# pady=10 คือการทำให้มีระยะห่างแนวบนล่าง 10 พิกเซล

B2 = ttk.Button(F1,text='กาแฟ',command=lambda x='coffee': Expense(x), style='my.TButton')
B2.grid(row=0,column=1,ipadx=20,ipady=10,padx=5)

B3 = ttk.Button(F1,text='ค่าแท็กซี่',command=lambda x='taxi': Expense(x), style='my.TButton')
B3.grid(row=0,column=2,ipadx=20,ipady=10,padx=5)


#########TABLE###########

header = ['วัน-เวลา','รายการ','จำนวนเงิน']

table_expense = ttk.Treeview(T1,column=header,show='headings',height=20)
table_expense.pack(pady=20)

table_expense.heading('วัน-เวลา',text='วัน-เวลา')
table_expense.heading('รายการ',text='รายการ')
table_expense.heading('จำนวนเงิน',text='จำนวนเงิน')


sum_expense = 0
sum_income = 0
sum_remaining = 0

def remaining():
	global sum_remaining
	cal = sum_income - sum_expense
	sum_remaining = float(cal)
	v_remaining.set('{:,.2f} บาท'.format(sum_remaining))
	UpdateGraph(sum_expense,sum_income)

def sum_table():
	global sum_expense
	allsum = []
	data = ReadCSV()
	for dt in data:
		#dt = [2020-06-27 17:00:03,ข้าว,20.0]
		allsum.append(float(dt[2]))
	v_allexpense.set('{:,.2f} บาท'.format(sum(allsum)))
	sum_expense = sum(allsum)

def sum_table2():
	global sum_income
	allsum = []
	data = ReadCSV2()
	for dt in data:
		#dt = [2020-06-27 17:00:03,ข้าว,20.0]
		allsum.append(float(dt[2]))
	v_allincome.set('{:,.2f} บาท'.format(sum(allsum)))
	sum_income = sum(allsum)

def update_table():
	data = ReadCSV()
	print(data)
	table_expense.delete(*table_expense.get_children()) 
	#clear ข้อมูลทั้งหมดในตาราง ก่อนการ insert
	for dt in data:
		table_expense.insert('','end',value=dt)
	sum_table()
	remaining()

def update_table2():
	data = ReadCSV2()
	print(data)
	table_income.delete(*table_income.get_children()) #ลบข้อมูลเก่าออกให้หมด
	#clear ข้อมูลทั้งหมดในตาราง ก่อนการ insert
	for dt in data:
		table_income.insert('','end',value=dt)
	sum_table2()
	remaining()
	
#อัพเดตรายการตอนรันครั้งแรก

############TAB2##############

v_income = StringVar() #เก็บรายการรายรับ
L = ttk.Label(T2,text='กรุณากรอกรายรับ').pack() #หัวข้อบนช่องกรอก
E21 = ttk.Entry(T2,textvariable=v_income, font=FONT1, width=30)
E21.pack(pady=10)

v_incomequan = StringVar() #เก็บจำนวนเงินรายรับ
L = ttk.Label(T2,text='รายรับ (บาท)').pack() #หัวข้อบนช่องกรอก
E22 = ttk.Entry(T2,textvariable=v_incomequan, font=FONT1, width=30)
E22.pack(pady=10)

def SaveIncome(event=None):
	print('บันทึกรายรับ')
	incm = v_income.get()
	incmq = float(v_incomequan.get())
	print('รายการ:', incm)
	print('จำนวนเงิน', incmq)
	print('---------')

	v_result2.set(f'กำลังบันทึกรายการ: {incm} จำนวนเงิน: {incmq:,.2f} บาท')

	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	data = [dt,incm,incmq] #จัดเรียงข้อมูลก่อนเซฟลง csv
	WritetoCSV2(data) #เรียกฟังชั่นการบันทึกข้อมูล

	#reset ตัวแปร
	v_income.set('')
	v_incomequan.set('')
	#ทำให้ cursor วิ่งไปหาช่องกรอกตัวแรก
	E21.focus()
	update_table2()

E22.bind('<Return>',SaveIncome) #หากมีการกดปุ่ม Enter ที่ช่องกรอกจำนวนเงิน จะทำการเรียกฟังชั่น

B21 = ttk.Button(T2,text='บันทึก',command=SaveIncome, style='my.TButton')
B21.pack(ipadx=20,ipady=10)


v_result2 = StringVar()
R2 = ttk.Label(T2, textvariable= v_result2, font=FONT2, foreground='green') # R1 = Label(fg='green')
R2.pack(pady=20)

header = ['วัน-เวลา','รายการ','จำนวนเงิน']

table_income = ttk.Treeview(T2,column=header,show='headings',height=6)
table_income.pack(pady=20)

table_income.heading('วัน-เวลา',text='วัน-เวลา')
table_income.heading('รายการ',text='รายการ')
table_income.heading('จำนวนเงิน',text='จำนวนเงิน')














############TAB3##############

v_allexpense = StringVar()

L = ttk.Label(T3,text='ยอดค่าใช้จ่ายทั้งหมด (บาท):',font=FONT3,foreground='orange').place(x=50,y=50)
LR1 = ttk.Label(T3,textvariable=v_allexpense,font=FONT3,foreground='orange')
LR1.place(x=400,y=50)


v_allincome = StringVar()

L = ttk.Label(T3,text='ยอดรายรับทั้งหมด (บาท):',font=FONT3,foreground='green').place(x=50,y=100)
LR2 = ttk.Label(T3,textvariable=v_allincome,font=FONT3,foreground='green')
LR2.place(x=400,y=100)

v_remaining = StringVar()

L = ttk.Label(T3,text='คงเหลือทั้งหมด (บาท):',font=FONT3,foreground='blue').place(x=50,y=150)
LR2 = ttk.Label(T3,textvariable=v_remaining,font=FONT3,foreground='blue')
LR2.place(x=400,y=150)










#try , except เป็นการดักจับ error ให้ลองทำใน try ก่อน
#หากรันแล้วไม่มีปัญหาก็ไม่รันใน except หากรันแล้วมีปัญหา ให้ไปทำงานใน except
try:
	update_table()
	update_table2()
except:
	print('ERROR')

GUI.mainloop() # ทำให้โปรแกรมรันได้ตลอดเวลา