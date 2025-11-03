a = []
hap = 0
i=0
while True:
    i+=1
    n = int(input("Enter number "+str(i)+" : "))
    if n == 0:
        break
    a.append(n)
    hap+=n

print("Total : ", hap)
print("Avg : ", hap/len(a))

