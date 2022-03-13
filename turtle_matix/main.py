import turtle
from turtle import Turtle, Screen
import random
import time

is_raining = True
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
turtle.colormode(255)
screen.setup(width=500, height=500)
x_positions = [0, -10, -20, 200, 190,  220, 110, 100, -40, -50,  150, 140,  210, -160, -170, -90, -100, 70, 60, -110,
               -120, 50, 40, 30, -200, 130, -60, -70, -80, 120, -140, -150, -230, -240,
               -180, -190, 240, 20, 10, 80, -30, 230, -130, -210, -220,  90, 180, 170, 160]
all_turtles = []


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, g, b)
    return rand_colour


poet = Turtle()
poet.pencolor(0, 255, 65)
poet.write("Welcome to the Turtle Matrix", align="center", font=("Arial", 20, "bold"))

for turtle_index in range(0, 49):
    new_turtle = Turtle()
    new_turtle.hideturtle()
    new_turtle.shape("turtle")
    new_turtle.shapesize(0.75)
    new_turtle.color(0, 255, 65)
    # new_turtle.speed("fastest")
    turtle.pensize(30)
    new_turtle.penup()
    new_turtle.goto(x=x_positions[turtle_index], y=250)
    new_turtle.setheading(270)
    all_turtles.append(new_turtle)



while is_raining:
    screen.update()
    time.sleep(0.1)
    for turtle in all_turtles:
        turtle.pencolor(random_colour())
        turtle.showturtle()
        turtle.pendown()
        # turtle.speed("fastest")
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)
        # time.sleep(1)

screen.exitonclick()
