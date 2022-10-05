#template-center.py

from tkinter import *
from tkinter import ttk

GUI = Tk() # นี่คือหน้าต่างหลักของโปรแกรม
GUI.title('ตัวอย่าง')
GUI.iconbitmap('wallet.ico')

w = 500
h = 300

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #ปรับขนาด
#GUI.state('zoomed')

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
    url = 'https://www.uncle-engineer.com'
    webbrowser.open(url)

from tkinter import messagebox as msb

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About', command=About)
helpmenu.add_command(label='Donate',command=lambda: msb.showinfo('Donate','เลขบัญชี: 700 258 444\nธนาคารกรุงไทย'))
#command=lambda: msb.showinfo('Donate','เลขบัญชี: 700 258 444\nธนาคารกรุงไทย')


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


GUI.mainloop() # ทำให้โปรแกรมรันได้ตลอดเวลา