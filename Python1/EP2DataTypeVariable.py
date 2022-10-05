#Data Type Variable

#integers (int) = จำนวนเต็ม
#floating point (float) = ทศนิยม
#string (str) = ตัวอักษร ตัวเลขที่ไม่มีการคำนวณทางคณิตศาสตร์
#lists (list) = แสดงผลเป็น Object หรือ โครงสร้าง
#sets (set) = a b c x y z
#booleans (bool) = True False

#ชื่อตัวแปร = ค่าที่เก็บในตัวแปร
x = 19 #เป็น Integer อยู่
y = 2548
z = True
print(x)
# print("Ans" +  x)  ไม่ได้เพราะคนละ Type กัน ต้องแปลงก่อน
print("Ans \t" + str(x)) #ข้อความถือเป็น string เลยต้องเปลี่ยนเป็น str
print(y)
print(z)

print(" \n ")

#Type Conversion
#อยากรู้ว่าเป็น Type อะไร
print(type (y))
print(type (z))
print(type ("ShinakritLao"))
print(type ("19062548"))
print(type (19062548))

print(" \n " )

a = 19
b = 6
c = 6.48
Ans1 = a + b
Ans2 = a + c
print(Ans1)
print(type(Ans1))
print(Ans2)
print(type(Ans2))
#ถ้าอยู่ใน "19" หรือ "6" มันถืเป็นข้อความไม่ใช่ตัวเลขไม่สามารถนำมาคิดเลขได้

print(" \n ")

#ต้องแปลงก่อน string => integer
m = 0.6
n = "19"
#int(n)
Ans3 = m + int(n)
print(Ans3)
print(type(Ans3))

print(" \n ")

#ต้องแปลงก่อน integer => string
p = 20
q = "21"
Ans4 = str(p) + q
print(Ans4)
print(type(Ans4))

print(" \n ")

#ต้องแปลงก่อน string => float | integer => float | float => string | float => integer
t = 2548
d = "20"
e = 20.1
f = 20.5
print(float(d)) #เพิ่มทศนิยมเข้าไป
print(float(t)) #เพิ่มทศนิยมเข้าไป
print(str(e))   #เลขที่ไม่มีการคำนวณทางคณิตศาสตร์
print(str(f))   #เลขที่ไม่มีการคำนวณทางคณิตศาสตร์
print(int(e))   #เกิน 5 ไม่ปัด
print(int(f))   #เกิน 5 ไม่ปัด

print(" \n ")

g = float(d)
print(g)
print(type(g))