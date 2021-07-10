import turtle
s = turtle.Turtle('classic')
s.setheading(90)
s.speed()
s.hideturtle()
len = 200
angle = 45
s.pensize(5)

def setpensize(len):
    ps = 0
    if len == 200:
        ps = 5
    elif len >= 150 and len < 200:
        ps = 4
    elif len >= 100 and len < 150:
        ps = 3
    elif len >= 50 and len < 100:
        ps = 2
    else:
        ps = 1
    return ps

def TreeR(len):
    s.fd(len)
    hold = s.pos()
    if len == 200:
        s.pensize(5)
    elif len >= 150 and len < 200:
        s.pensize(4)
    elif len >= 100 and len < 150:
        s.pensize(3)
    elif len >= 50 and len < 100:
        s.pensize(2)
    else:
        s.pensize(1)
    if len > 4:
        s.rt(angle)
        TreeR(len*0.67)
        s.setpos(hold)
        s.lt(angle)
        TreeR(len*0.67)
        s.setpos(hold)

def TreeL(len):
    s.fd(len)
    hold = s.pos()
    if len == 200:
        s.pensize(5)
    elif len >= 150 and len < 200:
        s.pensize(4)
    elif len >= 100 and len < 150:
        s.pensize(3)
    elif len >= 50 and len < 100:
        s.pensize(2)
    else:
        s.pensize(1)
    if len > 4:
        s.lt(angle)
        TreeL(len*0.67)
        s.setpos(hold)
        s.rt(angle)
        TreeL(len*0.67)
        s.setpos(hold)

for i in range(8):
    s.rt(i*45)
    TreeR(len)
    s.setpos(0,0)
    TreeL(len)
    s.setpos(0,0)
    



##spiral to the center
##startlength = 200
##for i in range (100):
##    steve.fd(startlength)
##    steve.left(45)
##    startlength -= 2

##creates a star
## s.color('red', 'yellow')
## s.begin_fill()
## while True:
##     s.forward(200)
##     s.left(170)
##     if abs(s.pos()) < 1:
##         break
## s.end_fill()
## s.done()
