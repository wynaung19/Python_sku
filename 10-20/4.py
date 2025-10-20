i,num = 0,0

#num = int(input("Dan for : "))

for i in range(1,11):
    for j in range(1,11):
        print("%dX%2d=%3d" % (j,i,j*i),end=" | ")
    print("\n")

