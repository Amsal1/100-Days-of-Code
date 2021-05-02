from turtle import Screen, Turtle, colormode
import random

tim = Turtle()
colormode(255)
tim.speed(0)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colaar = (r,g,b)
    return colaar

for num in range(0,361, 5):
    tim.pencolor(random_color())
    tim.seth(num)
    tim.circle(50)


screen = Screen()
screen.exitonclick()