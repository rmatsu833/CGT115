import turtle
import time
import tkinter
t = turtle.Turtle()


t.pendown()
t.right(60)
t.forward(75)

t.right(120)
t.forward(75)

t.right(120)
t.forward(75)

t.penup()

t.right(60)
t.forward(100)

t.pendown()

i = 1
while i<=8:
    t.forward(30)
    t.right(45)
    i += 1


t.penup()


t.forward(100)

t.pendown()

i = 1
while i<=6:
    t.forward(40)
    t.right(60)
    i += 1

t.penup()




time.sleep(20)