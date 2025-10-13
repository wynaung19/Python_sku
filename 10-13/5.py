i = 0
while i < 3 :
    a = int(input("Enter score : "))

    if a > 50 :
        if a < 100:
            print("Greater than 50")
        else:
            print("Your IQ is less than 0")
    else:
        print('Less than 50')
    i+=1
