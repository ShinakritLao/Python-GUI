#ตัวดำเนินการทางตรรกศาสตร์

#AND =  และ
#OR  =  หรือ
#NOT = นิเสธ / ไม่

# คำตอบที่ได้ => จริง | เท็จ

x = (10 > 5)   #ค่า x = bool
y = (10 == 5)  #ค่า y = bool
z = x and y
# z = (10 > 5) and (10 == 5)
print(z)
print(not z)