#Jason Guan
#U9893-2926
#Program intended to draw a polygon when given the number of sides and length of each side.
#program will also label each polygon after drawing

import turtle

SideNum = int(input('Enter a number between 3 and 12 (inclusive): '))
while SideNum < 3 or SideNum > 12:
    SideNum = int(input('Invalid number of side. Enter a number between 3 and 12 (inclusive):'))
    
Angle = 180 - ((180 * (SideNum - 2))/SideNum)

SideLength = int(input('Enter the length of each side(>50): '))
while SideLength < 50:
    SideLength = int(input('Enter a larger length of each side: '))

x, y = 0, 0
turtle.penup()
turtle.setpos(x,y)
if SideNum == 3:
    turtle.write('Triangle' , font = 10)
elif SideNum == 4:
    turtle.write('Quadrilateral' , font = 10)
elif SideNum == 5:
    turtle.write('Pentagon' , font = 10)
elif SideNum == 6:
    turtle.write('Hexagon' , font = 10)
elif SideNum == 7:
    turtle.write('Heptagon' , font = 10)
elif SideNum == 8:
    turtle.write('Octagon' , font = 10)
elif SideNum == 9:
    turtle.write('Nonagon' , font = 10)
elif SideNum == 10:
    turtle.write('Decagon' , font = 10)
elif SideNum == 11:
    turtle.write('Hendecagon' , font = 10)
else:
    turtle.write('Dodecagon' , font = 10)
    
for x in range(SideNum):
    turtle.pendown()
    turtle.forward(SideLength)
    turtle.left(Angle)


