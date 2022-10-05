age = int(input("Your age : "))

if age <= 15 :
    if age == 15 :
        print("M.3")  #ถ้าไม่ต้องการให้มีการทำงานให้ใช้ pass แทน
    elif age == 14:
        print("M.2") #ถ้าไม่ต้องการให้มีการทำงานให้ใช้ pass แทน
    elif age == 13 :
        print("M.1") #ถ้าไม่ต้องการให้มีการทำงานให้ใช้ pass แทน
    else :
        print("ประถม")
else :
    print("ม.ปลาย")
