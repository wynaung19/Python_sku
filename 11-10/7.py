park=[]
top=0
park.append('car1')
top+=1
park.append('car2')
top+=1
park.append('car3')
top+=1
print(park)

print(len(park))

out = park.pop()
top-=1
print(out)

print(park)
print(len(park))

park.pop()
top-=1
print(park)
print(len(park))

park.pop()
top-=1
print(park)
print(len(park))
