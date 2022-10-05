data = {"191":"แจ้งเหตุด่วน" , "รถโรงพยาบาล":"รถโรงพยาบาล" , "1447":"ดับเพลิง"}

def searchNumber(message):
    for key , value in data.items() :
        if value==message:
            print("เบอร์ติดต่อ = " , key)
            break
        else :
            print("ไม่มีข้อมูล")
            break

message=input("ป้อนข้อมูลที่ต้องการ = ")
searchNumber(message)