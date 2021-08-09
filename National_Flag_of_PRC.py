# National_Flag_of_PRC.py
# This program can be used to paint the national flag of People's Republic of China.
import turtle as t
import math as m

pi = 3.14159265

def drawStar(cx, cy, r, angle): # center x, center y; radius; angle
    t.fillcolor("yellow")
    t.pencolor("yellow")
    t.pensize(1)
    l = 2 * r * (m.sin(0.4 * pi))
    t.penup()
    t.goto(cx, cy)
    t.pendown()
    t.seth(angle)
    t.fd(r)
    t.begin_fill()
    t.right(162)
    t.fd(l)
    for i in range(4):
        t.right(144)
        t.fd(l)
    t.end_fill()

n = eval(input("Please enter the width of the PRC national flag: "))
l = n / 30

t.screensize(2, 2, "red")
t.setup(n, n*2/3)
drawStar(-10*l, 5*l, 3*l, 90)
a1 = 180 + (m.atan2(3, 5)) * 180 / pi
drawStar(-5*l, 8*l, l, a1)
a2 = 180 + (m.atan2(1, 7)) * 180 / pi
drawStar(-3*l, 6*l, l, a2)
a3 = 180 - (m.atan2(2, 7)) * 180 / pi
drawStar(-3*l, 3*l, l, a3)
a4 = 180 - (m.atan2(4, 5)) * 180 / pi
drawStar(-5*l, l, l, a4)
t.done()