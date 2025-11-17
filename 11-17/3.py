while True:
    def calc(a,b,o):
        res = 0.0
        if o == '+':
            res = a+b
        elif o == '-':
            res = a-b
        elif o == '*':
            res = a*b
        elif o == '/':
            res = a/b
        return res
    r = 0
    x,y,op = 0,0,''
    x = int(input("0 = exit\nNUM1 : "))
    if x == 0:
        print("END")
        break
    op = input("+,-,*,/ : ")
    y = int(input("NUM2 : "))

    r = calc(x,y,op)
    print("%d %s %d = %.2f\n" % (x,op,y,r))
        
