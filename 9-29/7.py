a = 100
res = 0
i = 0

for i in range(1,5) :
    res = a<<i
    print("%d << %d = %d" % (a,i,res))


for i in range(1,5) :
    res = a >> i
    print("%d >> %d = %d" % (a, i ,res))
