#ชื่อใน parameter มีได้หลายชื่อ
def add(*number) :
    sum = 0
    for i in range(len(number)) :
        sum+=number[i]
    print(sum)

def displayData(**item) :
    print(item)

displayData(fname="Shin",lname="Lao")
displayData(fname="Shin",lname="Lao",city="Bang")
displayData(fname="Shin",lname="Lao",status="Single")
displayData(fname="Shin",lname="Lao",city="Bang",status="Single")
displayData(fname="Shin",lname="Lao",city="Bang",status="Single",job="Student")
displayData(fname="Shin")
displayData(fname="Shin",lname="Lao",country="Thailand")