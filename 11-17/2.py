while True:
    def plus(x,y):
        res = 0
        res = x+y
        return res

    hap = 0
    a = int(input("0=exit\nNum1 : "))
    if a == 0:
        print("End")
        break
    b = int(input("Num2 : "))
    hap = plus(a,b)
    print("RES : %d\n" % hap)
