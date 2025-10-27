ch = ""
a ,b = 0,0

while True:
    a = int(input("Num1 : "))
    if(a == 0):
        break;
    ch = input("CH : ")
    b = int(input("Num2 : "))
    if(ch == "+"):
        print("%d + %d = %d" % (a,b,a+b))
    elif(ch == "-"):
        print("%d - %d = %d" % (a,b,a-b))
    elif(ch == "*"):
        print("%d * %d = %d" % (a,b,a*b))
    elif(ch == "/"):
        print("%d / %d = %.2f" % (a,b,a/b))
    else:
        print("error")

print("END")


