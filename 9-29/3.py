while(True) :
    money,c500,c100,c50,c10 = 0,0,0,0,0

    money = int(input("Money : "))
    c500 = money // 500
    money %= 500
    c100 = money // 100
    money %= 100
    c50 = money  // 50
    money %=50
    c10 = money // 10
    money %=10

    print("\n500 -> %d" % c500)
    print("\n100 -> %d" % c100)
    print("\n50 -> %d" % c50)
    print("\n10 -> %d" % c10)
    print("\nLeft : %d\n" % money)
