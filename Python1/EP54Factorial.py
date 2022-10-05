y=int(input("ป้อนค่า = "))
def factorial(number):
    if number==1:
        return number
    else :
        return number * factorial(number-1)

x=factorial(y)
print(x)