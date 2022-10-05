start = 1
stop = 5
sum = 0
avg = 0
while (start <= stop) :
    number = int(input("ป้อนตัวเลขของคุณ : "))
    sum+=number #บวกเลขที่ป้อนในแต่ละรอบ
    start+=1

avg = sum / stop
print("ผลรวม = " , sum)
print("ค่าเฉลี่ย = " , avg)