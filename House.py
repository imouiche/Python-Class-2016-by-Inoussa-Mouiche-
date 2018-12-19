 
""" embeded house """
from turtle import *
import timeit
import sys
from math import cos, sqrt

recorder = sys.stdout
f = file("Housetime.txt", 'w')
sys.stdout = f
start = timeit.default_timer()
width(2)
speed(0) # speed of the turtle
forward(50)
left(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
left(90)
forward(100)
left(90)
forward(180)
left(90)
forward(200)
left(90)
forward(180)
up()
backward(180)
left(135)
down()

# roof of the house
begin_fill()
color('green')
forward(sqrt(100**2 + 100**2))
right(90)
forward(sqrt(100**2 + 100**2))
end_fill()
up()
right(45)
forward(90)
right(90)
forward(20)
down()
# Window of the first house
begin_fill()
color('violetred')
forward(20)
right(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
end_fill()
up()
goto(0,0)
right(90)
forward(100)
right(180)
down()

# Embeded house
color('black')
forward(20)
left(90)
begin_fill()
color('blue')
forward(40)
right(90)
forward(20)
right(90)
forward(40)
end_fill()
color('black')
right(90)
forward(20)
up()
backward(20)
left(180)
down()

forward(60)
left(90)
up()
forward(100)
down()
left(90)
forward(100)
left(90)
forward(100)
up()
backward(100)
left(135)
down()
# Roof of the second house
begin_fill()
color('green')
forward(sqrt(50**2 + 50**2))
right(90)
forward(sqrt(50**2 + 50**2))
end_fill()

up()
right(45)
forward(40)
right(90)
forward(10)
down()
# Window of the second house
begin_fill()
color('red')
forward(20)
right(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
end_fill()
hideturtle()

stop = timeit.default_timer()
print stop-start

Im = getscreen()
Im.getcanvas().postscript(file="EmbadedHouse.eps")

sys.stdout = recorder
f.close()

