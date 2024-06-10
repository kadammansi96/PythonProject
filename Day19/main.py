import turtle
from turtle import Turtle, Screen
import random
screen = Screen()


# def move_forward():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space", fun=move_forward)



"""Etch a Sketch"""


# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards, "Up")
# screen.onkey(move_backwards, "Down")
# screen.onkey(turn_left, "Left")
# screen.onkey(turn_right, "Right")
# screen.onkey(clear, "c")
#

"""Turtle race"""
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race. Enter the color: ")
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
y_position = [-100, -70, -40, -10, 20, 50]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!. The {winning_color} turtle is winner")
            else:
                print(f"You lose!. The {winning_color} turtle is winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()
