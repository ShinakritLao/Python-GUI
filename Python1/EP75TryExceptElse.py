try :
    number1=int(input("ป้อนตัวเลข 1 : "))
    number2=int(input("ป้อนตัวเลข 2 : "))
    result=number1/number2
    print(result)
    print("โอนเงิน")
except Exception as e :
    print(e)
else :
    print("โอนเงินสำเร็จ")