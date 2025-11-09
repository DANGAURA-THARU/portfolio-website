import turtle
import time

t = turtle.Turtle()
t.speed(5)
t.color("red")
turtle.bgcolor("black")

# Draw left half
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.end_fill()

# Draw right half
t.begin_fill()
t.left(120)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Pause then animate break
time.sleep(1)
t.color("black")
t.pensize(10)

# Draw crack
t.penup()
t.goto(0, 50)
t.pendown()
t.right(60)

for i in range(10):
    t.forward(20)
    t.right(30 if i % 2 == 0 else -30)

t.hideturtle()
turtle.done()
