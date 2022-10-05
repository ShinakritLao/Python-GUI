num = int(input("Your Moneys : "))

if num >= 1000 :
    print("1000 บาท = " , num // 1000 ,"ใบ")
    num = num % 1000

if num >= 500 :
    print("500 บาท = " , num // 500 ,"ใบ")
    num = num % 500

if num >= 100 :
    print("100 บาท = " , num // 100 ,"ใบ")
    num = num % 100

if num >= 50 :
    print("50 บาท = " , num // 50 ,"ใบ")
    num = num % 50

if num >= 20 :
    print("20 บาท = " , num // 20 ,"ใบ")
    num = num % 20

if num >= 10 :
    print("10 บาท = " , num // 10 ,"เหรียญ")
    num = num % 10

if num >= 5 :
    print("5 บาท = " , num // 5 ,"เหรียญ")
    num = num % 5

if num >= 2 :
    print("2 บาท = " , num // 2 ,"เหรียญ")
    num = num % 2

if num >= 1 :
    print("1 บาท = " , num // 1 ,"เหรียญ")