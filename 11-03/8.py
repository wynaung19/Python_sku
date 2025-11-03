a=[];b=[];n=1
for i in range(0,3):
    for j in range(0,4):
        a.append(n)
        n+=1
    b.append(a)
    a=[]

for i in range(0,3):
    for k in range(0,4):
        print("%3d" % b[i][k],end=" ")

    print("")
