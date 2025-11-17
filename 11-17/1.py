t = 1
def t_fun(t):
    print()
    print("T0.1")
    print("T0.2")
    if t == 1:
        print("T1.1")
    elif t == 2:
        print("T1.2")
    elif t == 3:
        print("T1.3")
    else:
        print("T000000")
    print("T2")
while t > 0:
    t = int(input("Enter Task num. 1,2,3 \n0=exit : "))
    if t == 0:
        break
    t_fun(t)
    print("END")
    
