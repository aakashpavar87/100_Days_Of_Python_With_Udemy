from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
# for i in range(7):
#     timmy.forward(100)
#     timmy.right(100)
#     timmy.left(50)
# timmy.forward(100)

from prettytable import PrettyTable
my_table = PrettyTable()
my_table.add_column("Pokemon" , ["Pikachu" , "Squirtle" , "Charmender"])
my_table.add_column("Type" , ["Electric" , "Water" , "Fire"])
my_table.align = "c"
print(my_table)
print(my_table.align)
my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

