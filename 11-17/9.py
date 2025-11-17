def df(**p):
    for k in p.keys():
        print("%s --> %d" % (k,p[k]))

df(w=9,a=1,d=4,s=4)
