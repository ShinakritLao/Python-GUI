greeting = ["สวัสดี" , "Hi"  , "Hello" , "GoodBye"]
people = ["ก้อง" , "แก้ม" , "โจ้"]
result = []

#เขียนแบบปกติ
for x in greeting:
    for y in people:
        result.append(x+y)
print(result)
#เขียนแบบย่อ
result = [x+y for x in greeting for y in people]
print(result)   