'''
def randomNumber(x):
    if x=="100":
        print("Get Reward")
        return 1000
    else :
        print("Lost")
        return 0

money = randomNumber("100")
x=300
result=money-x
print("Money Reward = " , money)
print("Money Poblaby = " , result)
'''
'''
def randomNumber(x):
    if len(x)<3:
        return
    if x=="100":
        print("Get Reward")
        return 1000
    else :
        print("Lost")
        return 0

money = randomNumber("100")
print("Money Reward = " , money)
money = randomNumber("500")
print("Money Reward = " , money)
'''
#ต.ย.โปรแกรมเช็คหวย
