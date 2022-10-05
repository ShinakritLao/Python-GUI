'''
try
คำสั่งรันโปรแกรมปกติ
except
คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด
'''

try :
    number1=int(input("ป้อนตัวเลข 1 : "))
    number2=int(input("ป้อนตัวเลข 2 : "))
    result=number1/number2
    print(result)
except :
    print("โปรแกรมมีข้อผิดพลาด")

#ย่อ
try :
    number1=int(input("ป้อนตัวเลข 1 : "))
    number2=int(input("ป้อนตัวเลข 2 : "))
    result=number1/number2
    print(result)
except Exception as e:
    print(e)