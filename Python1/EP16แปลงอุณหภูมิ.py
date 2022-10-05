temp = input("Tmperature(Degree) : ") #45C
degree = int(temp[:-1]) #45C
unit = temp[-1].upper() #C

if unit == "C" :
    Ans = (9*degree)/5+32
    AnsUnit = "Fahrenheit"
if unit == "F" :
    Ans = (degree-32)*5/9
    AnsUnit = "Celsius"
print("แปลงอุณหภูมิ " , temp , " เป็น " , AnsUnit , " = " , Ans)