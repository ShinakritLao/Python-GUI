num = int(input("ขนาดกระดาน = "))
for row in range(num) :
    for column in range (num) :
        if (row + column) % 2 == 0 : #
            print("x" , end = " " ) # ย่อเป็น
        else :                      # print("x" , end = " " ) if (row + column) % 2 == 0 else  print("o" , end = " " )
            print("o" , end = " " ) #

    print(" ")