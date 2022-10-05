name = "SHINNYSHINE"

print(name)
print(name [0] )
print(name [1] )
print(name [2] )
print(name [3] )
print(name [4] )
print(name [5] )
print(name [6] )
print(name [7] )
print(name [8] )
print(name [9] )
print(name [10] )
print(name [0 : 4] )  #ข้างหน้า
print(name [-5 : ] )  #ข้างหลัง
print(name [-5 : -1]) #ข้างหลัง

print(" \n ") 

print(len(name))      #นับจำนวนค่า string (รวมเว้นวรรคด้วย)

print(" \n ") 

namestrip1 = "   SHIN   "
print(namestrip1)
print(len(namestrip1))
namestrip2 = namestrip1.strip()  #ลบช่องว่างซ้ายขวา
namestrip3 = namestrip1.lstrip() #ลบช่องว่างซ้าย
namestrip4 = namestrip1.rstrip() #ลบช่องว่างขวา
print(namestrip2)
print(len(namestrip2))
print(namestrip3)
print(len(namestrip3))
print(namestrip4)
print(len(namestrip4))

print(" \n ") 

nameup1 = "shin"
nameup2 = "ShiN"
namelow1 = "SHIN"
namelow2 = "sHIn"
print(nameup1.upper())   #ทั้งหมดตัวใหญ่
print(nameup2.upper())   #ทั้งหมดตัวใหญ่
print(namelow1.lower())  #ทั้งหมดตัวเล็ก
print(namelow2.lower())  #ทั้งหมดตัวเล็ก
print(nameup1.capitalize()) #ตัวแรกตัวใหญ๋

print(" \n ") 

namereplace = "1 SHINNY 1 SHINE 1"
print(namereplace.replace("SHINE" , "SHIN"))  #แทนคำนั้นๆ
print(namereplace.replace("1" , "2"))         #แทนค่าทั้งหมดที่ซ้ำ
print(namereplace.replace("1" , "2" , 1))     #แทนเฉพาะตัวแรก
print(namereplace.replace("1" , "2" , 2))     #แทนเฉพาะตัวแรก ตัวสอง
print(namereplace.replace("1" , "2" , 3))     #แทนเฉพาะตัวแรก ตัวสอง ตัวสาม

print(" \n ") 

inname = "ฉันไปซื้อกับข้าวที่ตลาด"
inx = "ข้าว" in inname         #เช็คข้อความว่ามีหรือไม่
iny = "ตลาด" in inname       #เช็คข้อความว่ามีหรือไม่
inz = "ต่างประเทศ" in inname   #เช็คข้อความว่ามีหรือไม่
print(inx)
print(iny)
print(inz)
if inx :
    innamenew = inname.replace("กับข้าว" , "ไข่")
print(innamenew)

print(" \n ") 

Fname = "Shinakrit"
Lname = "Laokittichai"
Agenum = "15"
เงิน = 196.196
Fullnameage = ("ชื่อ "+ Fname + " นามสกุล " + Lname + " อายุ " + Agenum) #การต่อข้อความตัวเลข string
print(Fullnameage)
text = "ชื่อ {} นามสกุล {} อายุ {}" #การต่อข้อความตัวเลข string นอกวงเล็บ
print(text.format(Fname , Lname , Agenum))
text = "ชื่อ {0} นามสกุล {1} อายุ {2} อาชีพ {3} เงิน {4}"    #การต่อข้อความตัวเลข string นอกวงเล็บ
print(text.format(Fname , Lname , Agenum , "นักเรียน" , เงิน))   #สามรถใช้กับ float int string
text = "ชื่อ {3} นามสกุล {2} อายุ {1} อาชีพ {0} เงิน {4:.2f}" #การต่อข้อความตัวเลข string นอกวงเล็บ แบบเลือกตำแหน่ง
print(text.format(Fname , Lname , Agenum , "นักเรียน" , เงิน))   #2f คือ float ทศนิยม 2ตำแหน่ง ปัดทศนิยมด้วย

print(" \n ")

numorwordcount = "1 2 1 3 2 4 1 4 5 6 1 5 8 4 6 4 7 1 3"
print(numorwordcount.count("1"))  #นับตวอักษร คำ ตัวเลข ประโยค ว่าซ้ำกันกี่ตัว/คำ

print(" \n ")

swith = "นายสมชาย สมหญิง"
if swith.startswith("นาย") :
    print("male")
else :
    print("female")
phonenum = "080 808 8888"
if phonenum.endswith("8888") :
    print("NUM8")
else :
    print("NUM0")