i,num = 0,0

for i in range(1,11):
    for j in range(1,11):
        if(j >9):
            print("%d x %2d = %3d" % (j,i,j*i),end=" | ")
        else:
            print("%d x %2d =%3d" % (j,i,j*i),end=" | ")
    print("\n")

