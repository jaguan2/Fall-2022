#Jason Guan
#U9893-2926
#Program intended to simulate tortoise vs hare using turtle module

import turtle
import random

hare = turtle.Turtle()
turt = turtle.Turtle()
hidden = turtle.Turtle()
hidden.hideturtle()
turt.shape("turtle")
turt.penup()
hare.penup()

hare.setpos(-100,50)
turt.setpos(-100,0)

StartLine = -100
HareMovement = StartLine
TurtMovement = StartLine
Time = 0

hidden.penup()
hidden.left(90)
hidden.setpos(StartLine,-25)
hidden.pendown()
hidden.forward(100)
hidden.write('Start', font = 5)
hidden.penup()


hidden.setpos(100,-25)
hidden.pendown()
hidden.forward(100)
hidden.write('End', font = 5)
hidden.penup()

hidden.setpos(-100, 200)
hidden.write("ON YOUR MARK... GET SET... GO!!!\n AND THEY'RE OFF", font = 1)


def Hare(movement):
    global HareMovement
    if movement == 3 or movement == 4:
        HareMovement += 7
        hare.forward(7)
    elif movement == 5:
        HareMovement -= 10
        if HareMovement < -100:
            HareMovement = StartLine
        else:
            hare.backward(10)
    elif movement >=6 and movement <=8:
        HareMovement += 1
        hare.forward(1)
    elif movement >=9 and movement <=10:
        HareMovement -= 2
        if HareMovement < -100:
            HareMovement = StartLine
        else:
            hare.backward(2)

    return HareMovement

def Turt(movement):
    global TurtMovement
    if movement >= 1 and movement <= 5:
        TurtMovement += 3
        turt.forward(3)
    elif movement == 6 or movement == 7:
        TurtMovement -=5
        if TurtMovement < -100:
            TurtMovement = StartLine
        else:
            turt.backward(5)
    else:
        TurtMovement += 1
        turt.forward(1)

    return TurtMovement

while HareMovement < 100 and TurtMovement < 100:
    Finish = 0
    Finish = Hare(random.randint(1,10))
    Time += 1
    if Finish >= 100:
        hare.setpos(100,50) 
        hidden.setpos(150, 25)
        hidden.write('Hare wins!', font = 5)
        hidden.setpos (0, -50)
        hidden.write(f"'Time' of race: {Time} 'seconds'")
        break
    Finish = 0
    Finish = Turt(random.randint(1,10))
    if Finish >= 100:
        turt.setpos(100,0)
        hidden.setpos(150, 25)
        hidden.write('Tortose wins!', font = 5)
        hidden.setpos (0, -50)
        hidden.write(f"'Time' of race: {Time} 'seconds'")
        break

        
    
    











    
    
