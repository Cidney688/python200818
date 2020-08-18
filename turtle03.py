import turtle
import time
a=turtle.Turtle()
b=turtle.Turtle()
a.pensize(5)
b.pensize(6)
a.color('lightblue') 

for i in range(360):
    a.left(1)
    a.forward(1)
    b.right(1)
    b.forward(1)

turtle.done()