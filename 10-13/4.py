a = 1
while True:
    a = int(input("Number : "))
    
    if a<0:
        break;

    if a %2 == 0:
        print("Even")
    else:
        print("ODD")
