import turtle
import random
import time

a = {
    }
xm = 0
ym = 0
dsf = 100
direct = 'right'
x = turtle.Screen()
x.screensize(10000, 2000)
maxx = 10000
maxy = 2000

def b(turt, r):
    turt.clear()
    z = turt.pos()
    turt.up()
    turt.goto(z[0], z[1]-r)
    turt.down()
    turt.circle(r)
    turt.up()
    turt.goto(z[0], z[1])

d = turtle.Turtle()
d.up()
d.hideturtle()

def right():
    global xm
    direct = 'right'
    xm += 2
def left():
    global xm
    direct = 'left'
    xm -= 2
def up():
    global ym
    direct = 'up'
    ym += 2
def down():
    global ym
    direct = 'down'
    ym -= 2

def move():
    aa = d.pos()
    xn = aa[0] + xm
    yn = aa[1] + ym
    d.goto(xn, yn)

def movement():
    move()
    c = d.clone()
    c.down()
    c.hideturtle()
    a[c] = 10
    e = a.keys()
    ee = list(e)
    ee.reverse()
    for f in ee:
        f.clear()
        if not a[f] > max_ring_size:
            f.up()
            f.bk(1)
            f.down()
            b(f , a.get(f))
            if wavy_waves:
                a[f] += 10 + random.randint(-1, 1)*wavyness
            else:
                a[f] += 10
        else:
            a.pop(f)
    turtle.update()
    turtle.ontimer(movement)

def zero():
    global xm, ym
    xm = 0
    ym = 0
    d.home()

turtle.tracer(0, 0)

turtle.listen()
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(zero, '0')


#customisable options

wavy_waves = True
wavyness = 1
max_ring_size = 200


movement()
turtle.done()
