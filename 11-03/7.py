a = [20,10,30]
print(a)
a.append(40)
print("append 40" ,a)
print(a.pop())
print(a)

a.sort()
print("sort",a)

a.reverse()
print("rev",a)

print("index 20 : ", a.index(20))

a.insert(2,222)
print("insert(2,222)",a)

a.remove(222)
print("rem(222)",a)

a.extend([77,88,77])
print("extend([77,88,77])",a)

print("77 count :",a.count(77))
