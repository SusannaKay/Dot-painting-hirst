# import colorgram
# colors = []
# color_list = colorgram.extract('image.jpg', 40)
#
# for color in color_list:
#     my_tuple = color.rgb[0],color.rgb[1],color.rgb[2]
#     colors.append(my_tuple)
# print(colors)

import random

from turtle import Turtle, Screen, colormode
from random import choices
timmy = Turtle()
colormode(255)
timmy.penup()

color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]

timmy.goto(-200,-150)

def dot_line():
    for dot in range(0, 9):
        color = random.choice(color_list)
        timmy.dot(20, color)
        timmy.forward(50)
    color = random.choice(color_list)
    timmy.dot(20, color)
def turn_around():
    timmy.setheading(90)
    timmy.forward(50)
    if timmy.xcor() > 0:
        timmy.setheading(180)
    else:
        timmy.setheading(0)

for x in range(0,10):
    dot_line()
    turn_around()





screen = Screen()
screen.exitonclick()