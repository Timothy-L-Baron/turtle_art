"""Have the turtle draw borders around the screen. The first border will be around the outer perimeter
of the screen, each new border be drawn smaller inside the previous and in a different color"""

"""A dizzying array of turtleness - this one was fun to make as a trippy art piece!!!"""

import turtle
import random

colors = ['blue','green','orange','red','cyan','purple','white','yellow','pink','light blue','silver','gold', 'darkblue']

def random_color():
    for i in range(1):
        for color in random.sample(colors, len(colors)):
            x = color
            print(x)
            return x

wn = turtle.Screen()      # creates a graphics window
wn.bgcolor("lightgreen")  # set the window background colors

arnold = turtle.Turtle()  # create a turtle named arnold
arnold.hideturtle()
arnold.speed(0)
arnold.pensize(10)
arnold.penup()

aleena = turtle.Turtle()
aleena.hideturtle()
aleena.speed(0)
aleena.pensize(6)

arnold.forward(624)         # tell arnold to move forward 
arnold.left(90)
arnold.pendown()

aleena = turtle.Turtle()
aleena.hideturtle()
aleena.pensize(6)
aleena.speed(0)                 

gate = 'open'
x = 1
z = 0
w = 0

for i in range(15):  #original = 5
    y = 25
    arnold.forward(530/x)          # complete the second side of a rectangle
    arnold.left(90)
    if gate =='closed':
        gate = 'lap2'
    if gate == 'open':
        arnold.forward(1258/x - z)
        gate = 'closed'
    if gate =='lap2':
        arnold.forward(1260/x - z)
    arnold.left(90)
    arnold.forward(1057/x)
    arnold.left(90)
    if gate == 'closed':
        arnold.forward(1258/x - z)
    if gate == 'lap2':
        arnold.forward(1260/x - z)
    arnold.left(90)
    arnold.forward(528.5/x)   #528.5
    arnold.left(90)
    arnold.penup()
    arnold.forward(25+y)
    arnold.pendown()
    arnold.right(90)
    y = y + 25
    x = x + .05
    z = y + z
    w = w + 25
    arnold.color(random_color())
    aleena.color(random_color())
    for i in range(15): #original = 5
      aleena.circle(50*i)
      aleena.up()
      aleena.sety((50*i)*(-1))
      aleena.down()
    wn.bgcolor(random_color())

wn.exitonclick()
