import turtle as tt
import numpy as np
import keyboard

tt.setup(width=1050, height=1050)
t = tt.Turtle()

t.shape("classic")
t.color('#aaaaaa')
t.speed(0)

env = np.zeros((100, 100))

for i in range(-50, 51):
    t.penup()
    t.goto((-500, i * 10))
    t.pendown()
    t.forward(1000)
    t.right(90)

    t.penup()
    t.goto((i * 10, 500))
    t.pendown()
    t.forward(1000)
    t.left(90)

t.penup()
t.goto((0, 0))

pressed = None

while True:
    if keyboard.is_pressed('right') and pressed != 'right':
        t.setheading(0)
        t.forward(10)
        pressed = 'right'

    elif keyboard.is_pressed('left') and pressed != 'left':
        t.setheading(180)
        t.forward(10)
    elif keyboard.is_pressed('up') and pressed != 'up':
        t.setheading(90)
        t.forward(10)
    elif keyboard.is_pressed('down') and pressed != 'down':
        t.setheading(270)
        t.forward(10)
    else:
        pressed = None
