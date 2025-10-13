import turtle

swidth,sheight = 500,500;

turtle.title("Test")
turtle.shape('turtle')
turtle.setup(width=swidth+50,height = sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.goto(0,-sheight/2)
turtle.pendown()
turtle.speed(0)

for i in range(100):
    if i%3 == 0:
        turtle.pencolor('red')
    elif i%3 == 1:
        turtle.pencolor('green')
    else:
        turtle.pencolor('blue')
    #turtle.forward(3)
    turtle.circle(i*2)
    
turtle.done()
