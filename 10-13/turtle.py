import turtle as t

swidth,sheight = 500,500;

t.title("Turtle")
t.shape('turtle')
t.setup(width=swidth+50,height = sheight+50)
t.screensize(swidth,sheight)
t.penup()
t.goto(0,-sheight/2)
t.pendown()
t.speed(0)

for i in range(100):
    if i%3 == 0:
        t.pencolor('red')
    elif i%3 == 1:
        t.pencolor('green')
    else:
        t.pencolor('blue')
    #t.forward(3)
    t.circle(i*2)

t.done()
