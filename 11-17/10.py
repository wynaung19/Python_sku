import random as r

def getNum():
    return r.randrange(1,46)

lotto = []
num = 0

while True:
    num = getNum()
    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto) >= 6:
        break

print("RES ===> ",end='')
lotto.sort()
for i in range(0,6):
    print(lotto[i],end=' ')
