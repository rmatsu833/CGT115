import turtle
import time

t = turtle.Turtle()
a = 0



for l in range(9):

    for i in range(4):
        t.right(90)
        t.forward(10 + a)
        a += 2.5



time.sleep(10)