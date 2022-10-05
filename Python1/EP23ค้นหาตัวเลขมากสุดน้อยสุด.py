max = 0
min = 0
while True :
    num = int(input("ป้อนตัวเลข : "))
    #กระโดดออกจาก Loop
    if num < 0 :
        break
    if num > max :
        max = num
print("ค่าสูงสุด = " , max)
print("ค่าต่ำสุด = " , min)