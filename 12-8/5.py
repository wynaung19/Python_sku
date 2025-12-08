class Car:
    speed = 0
    def upSpeed(self,val):
        self.speed += val
        print("speed : %d" % self.speed)

class Sedan(Car):
    def upSpeed(self,val):
        self.speed += val
        if self.speed >= 150:
            self.speed = 150
            print("Speed (sub) : %d" % self.speed)

class Sonata(Sedan):
    pass

class Truck(Car):
    pass


se , tr , so = None,None,None

tr = Truck()
se = Sedan()
so = Sonata()

print("Truck ",end = "")
tr.upSpeed(200)

print("Sedan ",end = "")
se.upSpeed(150)

print("Sonata ",end = "")
so.upSpeed(150)



