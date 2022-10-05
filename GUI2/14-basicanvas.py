from tkinter import *
from tkinter import ttk
GUI = Tk()
GUI.geometry('500x400')
G = Canvas(GUI,width=400,height=300)
G.place(x=0,y=50)


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

	L = ttk.Label(GUI,text='รายจ่าย').place(x=50,y=360)
	L = ttk.Label(GUI,text='รายรับ').place(x=150,y=360)
	L = ttk.Label(GUI,text='คงเหลือ').place(x=250,y=360)
# G.delete(b2)
# G.delete(b2)
# G.delete(ALL)
UpdateGraph(1000,5000)

GUI.mainloop()