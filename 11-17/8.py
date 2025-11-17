def pf(*p):
    res = 0
    #print(type(p))
    for num in p:
        print(num)
        res = res + num
    print('RES')
    return res

hap = 0
hap = pf(10,20)
print(hap)
hap = pf(10,20,30,40,50,60,70,80,90,100)
print(hap)
