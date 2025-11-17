def mul(a,b):
    rl=[]
    r1=a+b
    r2=a-b
    rl.append(r1)
    rl.append(r2)
    return rl

ml = []
hap,sub = 0,0

ml = mul(100,200)
hap = ml[0]
sub = ml[1]
print("hap : %d , sub = %d" % (hap,sub))
