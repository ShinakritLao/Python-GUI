fruitA = {"banana" , "lime" , "lemon"}
fruitB = {"mango" , "pineapple , apple"}

#Union
AllFruit = fruitA.union(fruitB)
print(AllFruit)

#Update
fruitA.update(fruitB)
print(fruitA)

#Copy
fruitC = fruitB.copy()
print(fruitC)

#Difference
fruitD = fruitA.difference(fruitB)
print(fruitD)

#Intersection
fruitA.intersection_update(fruitB)
print(fruitA)

print(" \n ")

#subset
fish = {"ปลาดุก" , "ปลาหมอ" , "ปลาวาฬ" , "ปลาโลมา" , "ปลาฉลาม" , "ปลาตะเพียน"}
x = {"ปลาดุก" , "ปลาฉลาม"}
y = {"ปลาหมอ" , "ปลาวาฬ"}
print(x.issubset(fish))
print(fish.issuperset(x))