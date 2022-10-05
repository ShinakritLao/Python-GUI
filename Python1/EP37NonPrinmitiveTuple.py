tup = (1 , 3.14 , "Man1" , -2 , True , False) #ได้ทุกข้อมูล Tuple
print(tup) #เป็นข้อมูลที่ไม่สามารถเปลี่ยนแปลงได้ไม่เหมือนlistที่สามารถเปลี่ยนแปลงได้
print(type(tup))
print(tup[3])
print(tup[1:5])
print(tup[2: ])
print(tup[:4])
print(len(tup))

print(" \n ")

#ถ้าจะแก้ข้อมูลต้องเปลี่ยนเป็นlistก่อน
print("ก่อน" , tup)
lis=list(tup)
lis[0]="Shin"
tup=tuple(lis)
print("หลัง" , tup)

print(" \n ")

for item in tup :
    print("สมาชิก = " , item)

print(" \n ")

if "ทุเรียน" in tup :
    print("เป็นสมาชิก")
else :
    print("ไม่เป็นสมาชิก")
if True in tup :
    print("เป็นสมาชิก")
else :
    print("ไม่เป็นสมาชิก")

print(" \n ")

#tupleสามารถใช้เหมือน list ได้ทุกอย่างแค่แปรข้อมูลเป็น list
del tup #ลบตัวแปรทิ้งไปเลย\

print(" \n ")

num = (1234,4321,4444,True,"Shin",123.456,4,4)
x = num.count(4)
print(x)

print(" \n ")

#เรียงจากน้อยไปมาก
NumTup = (9,8,7,6,5,4,3,2,1,10,50,30,20,60,80,40,70,90,100)
print(NumTup)
NumLis=list(NumTup)
NumLis.sort()
NumTup=tuple(NumLis)
print(NumLis)
NumLis=list(NumTup)
NumLis.reverse()
NumTup=tuple(NumLis)
print(NumLis)

print(" \n ")

#นำtupleเปลี่ยนเป็นตัวแปร
number = (10,20,30)
a,b,c=number
d=a+c
print(a)
print(b)
print(c)
print(d)

print(" \n ")

#สลับtuple
n=(11,22)
m=(88,99)
print("Before",n)
print("Beforer",m)
m,n=n,m
print("After",n)
print("After",m)