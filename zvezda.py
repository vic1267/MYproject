import time
import turtle
turtle.shape('turtle')
turtle.color('green', 'red')
turtle.speed(10)
def david():
    for i in range(6):
        turtle.begin_fill()
        for x in range(3):
            turtle.forward(50)
            turtle.left(360 / 3)
        turtle.end_fill()
        turtle.forward(60)
        turtle.right(60)
david()
turtle.color('blue', 'green')
turtle.backward(200)
david()
turtle.color('green', 'yellow')
turtle.backward(-400)
david()
time.sleep(5)