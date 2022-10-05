fish = {"Salmon" , "Fish" , "Salmon" , "Seafish"}
print(fish) #จะไม่เอาตัวแปรที่ซ้ำกัน
fish.add("Mango")
print(fish)

for item in fish :
    print("ปลา" , item)

print(len(fish))

print("Salmon" in fish)
print("Gay" in fish)
print("Gay" not in fish)

fruit.remove("Seafish")
pritn(fish)
#ถ้าไม่มีให้ลบโดยใช้รีมูฟจะเออเรอแต่ถ้า discard จะปกติ
fruit.discard("Gay")
print(fish)

del fish