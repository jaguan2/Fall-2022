#Jason Guan
#U9893-2926
#Program intended to draw polygons when given the side and lengh of sides

import turtle

sides = int(input('Enter the number of sides between 3 and 12(inclusive):'))

while sides < 3 or sides > 12:
    sides = int(input('Invalid number of sides. Enter a number between 3 and 12 (inclusive):'))

length = int(input('Enter the length of each side (> 50):'))

while length < 50:
    int(input('Please enter a larger length of each side:'))

angle = 180 - ((180 * (sides-2)) / sides)

x, y = 0, 0
turtle.penup()
turtle.setpos(x,y)
for x in range(sides):
    turtle.pendown()
    turtle.forward(length)
    turtle.left(angle)

    
