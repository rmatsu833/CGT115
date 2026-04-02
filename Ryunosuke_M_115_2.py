import turtle
import time
import math

t = turtle.Turtle()
a = math.sqrt(3)



i = 1
while i < 5:
    t.forward(200)
    t.left(90)
    i += 1

t.penup()
t.forward(75)

#make a door
t.pendown()
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.penup()


t.left(90)
t.forward(75)
t.left(90)
t.forward(200)

#make a roof
t.pendown()
t.left(60)
t.forward(200 / a)
t.left(60)
t.forward(200 / a)
t.penup()

t.left(150)
t.forward(200)

t.left(150)
t.forward(20)

t.pendown()
t.right(60)
t.forward(70)
t.left(90)
t.forward(20 * a)
t.left(90)
t.forward(50)




time.sleep(5)

