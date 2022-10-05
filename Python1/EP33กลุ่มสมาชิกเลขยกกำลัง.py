number = [1,2,3,4,5,6,7,8,9,10]
print(number)

#เขียนแบบปกติ
for i in range(len(number)):
    number[i] = number[i]**2
print(number)
#เขียนแบบย่อ
number = [i*i for i in number]
print(number)