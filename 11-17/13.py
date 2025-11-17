from mod2 import *
import turtle as t

inStr = ''
swidth,sheight = 300,300
tx,ty,ta,ts = [0]*4

t.title('WaiYan')
t.shape('turtle')
t.setup(width = swidth+50, height = sheight+50)
t.screensize(swidth,sheight)
t.penup()
t.speed(5)

inStr = getString()

for ch in inStr:
    tx,ty,ta,ts = getXYAS(swidth,sheight)
    r,g,b = getRGB()
    t.goto(tx,ty)
    t.left(ta)
    t.pencolor((r,g,b))
    t.write(ch,font=("Turtle Racer",ts,'bold'))
t.done()
