sel = int(input("진수 : "))
num = input("Value : ")

if sel == 16:
    num10 = int(num,16)
if sel == 10:
    num10 = int(num,10)
if sel == 8:
    num10 = int(num,8)
if sel == 2:
    num10 = int(num,2)


print("16 ==> ",hex(num10))
print("10 ==> ",num10)
print("8  ==> ",oct(num10))
print("2  ==> ",bin(num10))
