select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

select = int(input("1 / 2: "))

if select == 1:
    numStr = input("Enter num : ")
    answer = eval(numStr)
    print("%s = %5.1f" % (numStr, answer))
elif select == 2:
    num1 = int(input("1st num : "))
    num2 = int(input("2nd num : "))
    for i in range(num1, num2 + 1):
        answer = answer + i
    print("%d + ... + %d = %d" % (num1, num2, answer))
else:
    print("Enter 1 or 2")
