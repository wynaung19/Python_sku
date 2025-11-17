h = lambda n1,n2 : n1 + n2
print(h(1,2))

h2 = lambda n1 = 10, n2 = 20 : n1+n2
print(h2())
print(h2(3,4))


ml = [1,2,3,4,5]
'''
def add10(num):
    return num +10

for i in range(len(ml)):
    ml[i] = add10(ml[i])
print(ml)
'''
add10 = lambda num : num+10
ml = list(map(add10,ml))
print(ml)

