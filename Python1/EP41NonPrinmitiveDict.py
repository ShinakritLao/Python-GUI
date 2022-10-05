#การสร้างDict
colors = {"red":"สีแดง" , 190:"สีเหลือง" , True:"สีเขียว"}
colors = dict({"red":"สีแดง" , 190:"สีเหลือง" , True:"สีเขียว"})
print(colors["red"])
print(colors[190])
print(colors[True])
colors.update({"blue":"สีน้ำเงิน" , "orange":"สีส้ม"})
print(colors)

for item in colors :
    print(item)
for item in colors.values() :
    print(item)
for item in colors.keys() :
    print(item)
for item in colors.items() :
    print(item)

del colors

print(" \n ")

shop = {
    "shop1" : {
        "Name" : "Shop1" ,
        "Menu" : ["Menu1.1" , "Menu1.2"] ,
        "zone" : "Zone1"
    } ,
    "shop2" : {
        "Name" : "Shop1" ,
        "Menu" : ["Menu2.1" , "Menu2.2"] ,
        "zone" : "Zone2"
    } ,
    "shop3" : {
        "Name" : "Shop3" ,
        "Menu" : ["Menu3.1" , "Menu3.2"] ,
        "zone" : "Zone3"
    }
}

print(shop)
print(" \n ")
print(shop["shop1"])
print(" \n ")
print(shop["shop1"]["Menu"])
print(" \n ")
print("Menu1.1" in shop["shop1"]["Menu"])
print(" \n ")
if "Menu1.1" in shop["shop1"]["Menu"] :
    print(true)
else : 
    print(false)