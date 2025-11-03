a = []
hap = 0

while True:
    n = int(input("Enter number : "))
    if n == 0:
        break
    a.append(n)
    hap+=n

print("Total : ", hap)
print("Avg : ", hap/len(a))

