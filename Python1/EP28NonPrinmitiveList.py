#เก็บข้อมูลแบบ Prinmitive
a=1
a1=2
a2=3
#เก็บข้อมูลแบบ NonPrinmitive : List
number = [ ] #list ว่าง
number = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9] #list number มีสมาชิก 1-9
name = ["Man1" , "Man2" , "Man3"] #list name มีสมาชิก 1-3
all = [1 , 3.14 , "Man1" , -2 , True , False] #ได้ทุกข้อมูล
print(type(all))  #list
#แสดงผล
'''
print(a) print(a1) print(a2)
print(number) print(name) print(all)
print(number[0]) #1 print(number[1]) #2 print(number[2]) #3
print(number[1:3]) #2,3 print(number[0:5]) #1,2,3,4,5
'''

print(" \n ")

#การแก้ไขข้อมูล
num = [1,2,3,4,5] #list มีสมาชิก 5 ตัว
print("ก่อนแก้ไข" , num)
num[4] = 10        #ถ้าใส่ สถานที่ข้อมูล(Index)ที่ไม่มี เช่น 5 จะ Error
num[-5] = "SHINNY" #ลบคือนับจากข้างหลังใช้ข้างบนก็ได้
print("หลังแก้ไข" , num)

print(" \n ")

#ประยุกต์กับ Loop For If
Num = [1,2,3,4,5,6,7,8,9]
thing = ["ลูกบอล" , "ลูกบาส"]
sum = 0
for x in Num :
    print("สมาชิก" , x , " = " , x)
    sum+=x #sum=sum+x
print(sum)

if 10 in Num :
    print("มีในNum")
else :
    print("ไม่มีในNum")
if "ลูกบาส" in thing :
    print("มีในThing")
else :
    print("ไม่มีในThing")

print(Num)
print(len(Num))   #ช็คจำนวนค่าในตัวแปร
print(thing)
print(len(thing)) #เช็คจำนวนค่าในตัวแปร
print(" \n ")
for i in range(len(thing)) :
    print(i)
    print(thing[i])

print(" \n ")

#ใช้ appendจะต่อท้าย insertแทรกตรงไหนก็ได้ เพิ่มข้อมูล
print("ก่อนเพิ่ม = " , thing)
thing.append("ลูกเทนนิส")
thing.append("ลูกปิงปอง")
print("หลังเพิ่ม = " , thing)
thing.insert(1 , "ลูกลูกวอลเลย์")
thing.insert(3 , "ลูกแบตมินตัน")
print("หลังแทรก = " , thing)

print(" \n ")

#ใช้ removeจะลบตัวนั้นออกทันที popลบข้อมูลที่อยู่หลังสุดออก 
# dellเลือกที่จะลบตัวแปรออกหรือลบข้อมูล clearลบเฉพาะข้อมูลข้างใน ลบข้อมูล
print("ก่อนลบ = " , thing)
thing.remove("ลูกปิงปอง")
print("หลังลบ = " , thing)
print(" \n ")
print("ก่อนลบหลังสุด = " , thing)
thing.pop()
thing.pop()
print("หลังลบหลังสุด = " , thing)
print(" \n ")
# del thing #ลบตัวแปรนี้ออกไปเลย
print("ก่อนลบDell = " , thing)
del thing[1]
print("หลังลบDell = " , thing)
print(" \n ")
thing.clear()
print("หลังClear = " , thing)

print(" \n ")

#การคัดลอกข้อมูล
thing = []
print(thing)
thing = Num.copy()
print(thing)

print(" \n ")

#การรวมข้อมูลต่อท้าย extend , (+)
allGroup = Num + thing
print(allGroup)
Num.extend(thing)
print(Num)

print(" \n ")

#แสดงจำนวนสมาชิก (Count)
Count = allGroup.count(5) #Integer Count
print(Count)