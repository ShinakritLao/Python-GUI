i = 1 #ตัวจำนวนรอบ
summation = 0 #ตัวนับจำนวนรอบ
average = 0 #ผลรวม / จำนวนรอบ
# 1 + 2 + 3 + 4 + 5
count = int(input("ระบุจำนวนรอบ : "))

while i <= count :
    summation = summation + i #เก็บผลรวมของ i แต่ละรอบ 1 + 2 + 3
    print("รอบที่ : " , i , "   ผมรวม : " , summation)
    i = i + 1 # 1 , 2 , 3 , 4 , 5
average = summation / count
print("ผลรอมการบวก : " , summation)
print("ค่าเฉลี่ย : " , average)