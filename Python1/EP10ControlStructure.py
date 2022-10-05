'''
โครงสร้งแบบควบคุม
1. แบบลำดับ  #ที่เคยเรียนมา 1-9
2. แบบเลือก  #(if)
3. แบบทำซ้ำ  #
'''

#if expression : 
#   statement

age = int(input("Your Age : "))

if age >= 20 and age <=30 : 
    print("วัยทำงาน")
elif age >= 15 and age <= 19 :
    print("วัยรุ่น")
elif not age <= 20 :
    print("วัยชรา")
else : 
    print("วัยเรียน")