import turtle
from turtle import *

# setting the screen for drawing
scr = turtle.Screen()
ttl = turtle.Turtle()
speed(10)

# Drawing the text first
turtle.color("black")  # Adjusted color
turtle.penup()
turtle.goto(10, -170)  # Adjusted position for middle of the same line
# turtle.pendown()
turtle.write("Happy Republic Day 2024", align="center", font=("Comic Sans MS", 18, "bold"))
# turtle.up()
turtle.goto(-30, -190)  # Adjusted position for middle of the same line
turtle.down()
ttl.hideturtle()
turtle.done()

# Defining the instance of turtle
ttl = turtle.Turtle()
speed(5)

# keeping the pen up initially
ttl.penup()
ttl.goto(-120, 100)  # Adjusted position for smaller size
ttl.pendown()

# Drawing the Orange Rectangle first
# and then the white rectangle
ttl.color("orange")
ttl.begin_fill()
ttl.forward(300)  # Reduced size
ttl.right(90)
ttl.forward(63)  # Reduced size
ttl.right(90)
ttl.forward(300)  # Reduced size
ttl.end_fill()
ttl.left(90)
ttl.forward(63)  # Reduced size

# now drawing the Green Rectangle
ttl.color("green")
ttl.begin_fill()
ttl.forward(63)  # Reduced size
ttl.left(90)
ttl.forward(300)  # Reduced size
ttl.left(90)
ttl.forward(63)  # Reduced size
ttl.end_fill()

# Drawing the central Big Blue Circle
ttl.penup()
ttl.goto(25, 0)  # Adjusted position for smaller size
ttl.pendown()
ttl.color("navy")
ttl.begin_fill()
ttl.circle(25)  # Reduced size
ttl.end_fill()

# Drawing the in-circle Big White Circle
ttl.penup()
ttl.goto(22, 0)  # Adjusted position for smaller size
ttl.pendown()
ttl.color("white")
ttl.begin_fill()
ttl.circle(22)  # Reduced size
ttl.end_fill()

# Drawing the Smaller Blue Circle
ttl.color("navy")
ttl.penup()
ttl.goto(5, 0)  # Adjusted position for smaller size
ttl.pendown()
ttl.begin_fill()
ttl.circle(5)  # Reduced size
ttl.end_fill()

# Drawing the 24 spokes of the Indian Flag
ttl.penup()
ttl.goto(0, 0)  # Adjusted position for smaller size
ttl.pendown()
ttl.pensize(1)
for j in range(24):
    ttl.forward(15)  # Reduced size
    ttl.backward(15)  # Reduced size
    ttl.left(15)

# Drawing the stick of the Indian flag
ttl.color("black")
ttl.pensize(5)  # Adjusted size
ttl.penup()
ttl.goto(-120, 100)  # Adjusted position for smaller size
ttl.right(180)
ttl.pendown()
ttl.forward(250)  # Reduced size

# to hide the turtle pen we used hideturtle
ttl.hideturtle()

# holding the output on the window
turtle.done()
