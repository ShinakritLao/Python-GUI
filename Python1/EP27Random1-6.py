import random
#สุ่มเลข
myrandom = random.randrange(1,7)
k=1
correct = False
print("คุณมีโอกาสตอบ 3 ครั้ง \n")
print(myrandom) #เฉลย
while True :
    number = int(input("ป้อนตำตอบของคุณ = "))
    correct = (number == myrandom) #True / False
    if not correct :
        if (number < myrandom) :
            print("น้อยไป")
        if (number > myrandom) :
            print("มากไป")

    if correct :
        print("ตอบถูก")
        break
    if number < 0 or k == 3 :
        break
    k = k+1
if not correct :
    print("โอกาสครบ 3 ครั้งแล้ว")
    print("เฉลย = " , myrandom)