def displayFood() :
    print("Rice")

def displayCity() :
    displayFood()
    print("Hello")


displayCity()



def equal(x,y,z) :
    return compareMax(compareMax(x,y),z)

def compareMax(x,y) :
    if x>y :
        return x
    else :
        return y

max=equal(3,6,-5)
print("Most Value = " , max)

