while True :
    try :
        number1=int(input("ป้อนตัวเลข 1 : "))
        number2=int(input("ป้อนตัวเลข 2 : "))
        if number1 == 0 and number2 == 0 :
            break
        result = number1/number2
        print(result)
    except ValueError:
        print("กรุณาป้อนตัวเลขด้วยครับ")
    except ZeroDivisionError:
        print("ห้ามหารด้วยศูนย์นะครับ")
    finally :
        print("ทำงานต่อไป...")