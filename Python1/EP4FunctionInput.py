#Function Input
name = input("your psassword : ")
print("password = " + name)
print(type(name))

print(" \n ")

FirstName = input("กรุณาป้อนชื่อของท่าน : ")
LastName  = input("กรุณาป้อนนามสกุลของท่าน : ")
print("ชื่อ-นามสกุล : " + FirstName + " \t " + LastName)
print(type(FirstName))
print(type(LastName))

print(" \n ")

x = input("ป้อนค่าที่ 1 : ") #เป็น string
y = input("ป้อนค่าที่ 2 : ") #เป็น string
wrong = x + y
print(wrong)
print(type(wrong))
z = int(x) + int(y) #ต้องแปลงเป็น integer เพราะถ้าเป็นค่า str จะไม่มีการคำนวณทางคณิตศาสตร์
print(z)
print(type(z))

##ย่อโค๊ด
# x = int(input("ป้อนค่าที่ 1 : ")) #เป็น string
# y = int(input("ป้อนค่าที่ 2 : ")) #เป็น string
# print(x + y)