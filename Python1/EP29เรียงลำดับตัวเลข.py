number = []
while True :
    x = int(input("ป้อนตัวเลข : "))
    if x == 0:
        break
    number.append(x)

print("ก่อนจัดลำดับ -> " , number)
number.sort()
print("จากน้อยไปมาก -> " , number)
number.reverse()
print("จากมากไปน้อย -> " , number)