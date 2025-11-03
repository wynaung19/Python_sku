a = [0,0,0,0]
hap = 0

for i in a:
    a[i] = int(input("Enter number : "))
    hap+=a[i]

print("Total : ", hap)
print("Avg : ", hap/len(a))
