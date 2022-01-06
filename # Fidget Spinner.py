# Fidget Spinner

from turtle import *
angleOffset = {"turn": 0}
def drawSpinner():
    clear()
    angle = angleOffset["turn"]/10
    right(angle)
    forward(100)
    dot(120, "#FB4B4E")
    back(100)
    right(120)
    forward(100)
    dot(120, "#3777FF")
    back(100)
    right(120)
    forward(100)
    dot(120, "#4D9078")
    back(100)
    right(120)
    update()

def animate():
    if(angleOffset["turn"] > 0):
        angleOffset["turn"] -= 1
    
    drawSpinner()
    ontimer(animate, 20)
def turn():
    angleOffset["turn"] += 10

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(turn, "space")
listen()
animate()
done()