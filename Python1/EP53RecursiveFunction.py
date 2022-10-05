#จะวนจนกว่าจะถูก return
y=int(input("ป้อนค่า = "))

def addNumber(number) :
    if number == 5:
        return
    print(number+1) #0
    number+=1 #1
    addNumber(number)

def summation(number) :
    if number == 1 :
        return number
    else :
        return number+summation(number-1)

x=summation(y) #5+4+3+2+1
print(x)