#ตัวดำเนินการทางคณิตศาสตร์
#ตัวดำเนินการ = Oprators = + - * / ** // % == < > 
#ตัวที่ถูกดำเนินการ = Operand = a b c x y z
x = int(input("ป้อนค่า x : "))
y = int(input("ป้อนค่า y : "))
print("ผลบวก" , x + y)
print("ผลลบ" , x - y)
print("ผลคูณ" , x * y)
print("ผลหาร" , x / y)
print("เลขยกกำลัง" , x **y)
print("ผลหารปัดเศษ" , x // y)
print("หารเอาเศษ mod" , x % y)

print(" \n ")

#ตัวดำเนินการเปรียบเทียบ
#ชนิดข้อมูลเหมือนกัน
#คำตอบ 2 คำตอบ => จริง | เท็จ
a = int(input("ป้อนค่า a : "))
b = int(input("ป้อนค่า b : "))
c = int(input("ป้อนค่า c : "))
print("ค่า a มากกว่าค่า b หรือไม่ ? : " , a > b)
print("ค่า a น้อยกว่าค่า b หรือไม่ ? : " , a < b)
print("ค่า a เท่ากับค่า b หรือไม่ ? : " , a == b)
print("ค่า a ไม่เท่ากับค่า b หรือไม่ ? : " , a != b)
print("ค่า a มากกว่า หรือ เท่ากับค่า b หรือไม่ ? : " , a >= b)
print("ค่า a น้อยกว่า หรือ เท่ากับค่า b หรือไม่ ? : " , a <= b)
print("ค่า a มากกว่าค่า b และ มากกว่า c หรือไม่ ? : " , a > b > c)
print("ค่า a น้อยกว่าค่า b และ น้อยกว่า c หรือไม่ ? : " , a < b < c)