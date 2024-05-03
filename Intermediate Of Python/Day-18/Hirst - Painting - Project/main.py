###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
#
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("images.jpeg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
tim = Turtle()
sc = Screen()
colors_rgb = [(190, 166, 125), (131, 84, 63), (78, 97, 119), (144, 160, 174), (162, 149, 59), (213, 202, 148), (70, 38, 30), (76, 105, 84), (116, 40, 31), (146, 170, 147), (105, 81, 86), (182, 100, 86), (55, 41, 43), (163, 150, 160), (42, 51, 63), (220, 179, 170), (106, 141, 125), (109, 37, 40), (104, 125, 156), (49, 75, 63), (184, 92, 95), (50, 62, 84), (69, 66, 52), (180, 201, 177), (40, 65, 52), (112, 136, 138)]

# tim.setheading(tim.heading() - 50)
# print(tim.heading())
tim.hideturtle()
tim.penup()
tim.setposition(-300, -150)
tim.pendown()
init_pos = tim.pos()
print(init_pos)
step = 25
for _ in range(10):
    for _ in range(10):
        tim.dot(10, random.choice(colors_rgb))
        tim.penup()
        tim.forward(25)
        tim.pendown()
    tim.up()
    tim.setposition((-300), (-150)+step)
    tim.down()
    step += 25


sc.exitonclick()
