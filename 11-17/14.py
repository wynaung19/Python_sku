'''
h = lambda n1,n2 : n1 + n2
print(h(1,2))

h2 = lambda n1 = 10, n2 = 20 : n1+n2
print(h2())
print(h2(3,4))


ml = [1,2,3,4,5]
def add10(num):
    return num +10

for i in range(len(ml)):
    ml[i] = add10(ml[i])
print(ml)
add10 = lambda num : num+10
ml = list(map(add10,ml))
print(ml)

def count(n):
    if n >= 1:
        print(n,end=' ')
        count(n-1)
    else:
        return

count(10)
def fact(n):
    if n <= 1:
        return n
    else:
        print(n)
        return n * fact(n-1)
print(fact(4))
'''
def genF():
    yield 1
    yield 2
    yield 'a'

print(list(genF()))

def fun(num):
    for i in range(0,num):
        yield i
        print('Gen...')
for data in fun(50):
    print(data)
