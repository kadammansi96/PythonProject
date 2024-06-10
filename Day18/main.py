from turtle import Turtle, Screen
import turtle as t
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("black")

"""Draw a square"""
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

"""Draw a dashed line"""

# for _ in range(15):
    # timmy_the_turtle.forward(10)
    # timmy_the_turtle.color("white")
    # timmy_the_turtle.forward(10)
    # timmy_the_turtle.color("black")

# #     OR
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

"""Drawing different shapes"""

# colours = ["light cyan", "cyan", "gray", "dark gray", "dark cyan", "dark olive green", "tomato",
#            "firebrick", "sandy brown", "navajo white"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)

"""Draw a random walk"""

# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# directions = [0, 90, 180, 270]
#
# for _ in range(100):
#     timmy_the_turtle.speed(30)
#     timmy_the_turtle.pensize(width=10)
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.setheading(random.choice(directions))


"""Draw a spirograph"""

timmy_the_turtle.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(50):
    timmy_the_turtle.width(2)
    timmy_the_turtle.circle(100)
    timmy_the_turtle.color(random_color())
    current_heading = timmy_the_turtle.heading()
    timmy_the_turtle.setheading(current_heading + 10)
    timmy_the_turtle.circle(100)

screen = Screen()
screen.exitonclick()