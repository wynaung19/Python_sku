i = 0
hap = 0.0

start = int(input("Start : "))
end = int(input("End : "))
chg = int(input("Inc or Dec : "))

for i in range(start,end - 1,chg):
    hap = hap +i
    print(i)

print("sum : %d" % hap)
