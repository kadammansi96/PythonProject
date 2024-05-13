# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
color_list = [(254, 253, 253), (178, 158, 130), (145, 166, 182), (37, 31, 26), (231, 240, 237), (197, 129, 152), (154, 189, 181), (249, 195, 49), (226, 87, 39), (230, 172, 190), (165, 65, 50), (120, 41, 33), (20, 115, 144), (124, 40, 61), (19, 45, 86), (170, 203, 205), (30, 66, 57), (59, 140, 75), (215, 226, 230), (239, 219, 225), (166, 204, 201), (62, 26, 45), (6, 79, 111), (135, 64, 86), (193, 102, 132), (21, 85, 61), (226, 176, 164), (36, 47, 99), (57, 70, 39), (84, 151, 99)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()