class Car:
    color=""
    speed = 0
    name = ""

    def upSpeed(self,value):
        self.speed += value

    def downSpeed(self,value):
        self.speed -= value
        
c1 = Car()
c1.color = "red"
c1.name = "L"
c1.speed = 9
print(c1.speed)
print(c1.color)
print(c1.name)
c1.upSpeed(3)
print(c1.speed)
print("-----------")
c2 = Car()
c2.color = "green"
c2.name = "A"
c2.speed = 4
print(c2.speed)
print(c2.color)
print(c2.name)
c2.upSpeed(2)
print(c2.speed)


c2.downSpeed(1)
print(c2.speed)
