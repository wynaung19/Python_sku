t1 = (10,20,30,40);t1
t2 = 10,20,30,40;t2
print(t1,t2)

t3 = (10);t3
t4 = 10;t4
t5 = (10,);t5
t6 = 10,;t6

print(t2,t3,t4,t5,t6)

## ERROR
'''
t1.append(40)
t1[0] = 40
del(t1[0])
'''
print(t1[0]+t1[1]+t1[2])
print(t1[1:3])
print(t1[1:])
print(t1[:3])

t2 = ('A','B')
print(t1+t2)
print(t2*3)

t = (10,20,30)
l = list(t)
l.append(40)
t = tuple(l)
print(t)
