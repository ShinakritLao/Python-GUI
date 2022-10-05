def displayFruit(item) :
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ = " , i+1 , " = " , item[i])

def displayVet(item) :
    for i in range(len(item)) :
        print("ผักชิ้นที่ = " , i+1 , " = " , item[i])

fruit = ["มะม่วง","มะละกอ","ฝรั่ง","มะนาว"]
vet = ('ชะอม','ผักกาด','คะน้า')

displayFruit(fruit)
displayVet(vet)