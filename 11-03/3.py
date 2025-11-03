a=[]
b=[]
n=0
for i in range(0,100):
    a.append(n)
    n+=2

for i in range(0,100):
    b.append(a[99-i])
    
for i in range(0,100):
    print(a[i],b[i],end="|")
