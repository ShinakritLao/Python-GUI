#ห้ามเซฟว่า turtle จะ error

import turtle
import random
tao = turtle.Turtle() #เรียกเต่า
color = ['red','blue','purple','green','orange'] #สามารถใช้โค๊ดสีได้
tao.pensize(5) #ขนาดเส้น

for i in range(10): #คำสั่งซ้ำ 10 ครั้ง
    c = random.choice(color) #หยิบสีจากข้างบนมาสุ่ม
    tao.color(c)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    #randomint = random integer คือ ให้สุ่ม -200 ถึง 200
    tao.penup() #ยกปากกาขึ้น
    tao.goto(x,y) #ไปที่ตำแหน่งที่สุ่ม
    tao.pendown() #วางปากการลง
    size = random.randint(50,100) #ขนาดสี่เหลี่ยม
    #randomint = random integer คือ ให้สุ่ม 50 ถึง 100
    for i in range(4): #วนซ้ำ 4 ครั้ง เพื่อทำสี่เหลี่ยม
        tao.forward(size) #เดินหน้า
        tao.left(90) #เลี้ยวซ้าย 90 องศา
