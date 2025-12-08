class Car:
    speed = 0
    name = ""
    count = 0

    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
        Car.count += 1

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed
        
c1,c2 = None, None

c1 = Car("audi",10)
c2 = Car("alphad",30)

print("%s speed : %d" % (c1.getName(),c1.getSpeed()))
print("%s speed : %d" % (c2.getName(),c2.getSpeed()))

print(Car.count)
