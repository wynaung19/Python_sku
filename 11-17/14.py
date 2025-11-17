h = lambda n1,n2 : n1 + n2
print(h(1,2))

h2 = lambda n1 = 10, n2 = 20 : n1+n2
print(h2())
print(h2(3,4))
