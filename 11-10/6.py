nl = [num * num for num in range(1,6)]
print(nl)

nl = [num for num in range(1,22) if num%3 == 0]
print(nl)

foods = ['f1','f2','f3','f4']
sides = ['s1','s2','s3']

for food,side in zip(foods,sides):
    print(food,'--->',side)

tupList = list(zip(foods,sides))
dic = dict(zip(foods,sides))
print(tupList)
print(dic)
