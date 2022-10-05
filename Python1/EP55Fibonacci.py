y=int(input("ป้อนค่า = "))
def fibonucci(number):
    if number<=1:
        #เลข 2 ลำดับแรก
        return number
    else :
        #เลขลำดับถัดไป
        return fibonucci(number-1) + fibonucci(number-2)

for i in range(y) : 
    print(fibonucci(i))