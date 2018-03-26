#P4T1a
#Shapes
#Sutcliffe
#March 23, 2018

import turtle
wn = turtle.Screen()

tess = turtle.Turtle()
tess.color('pink')
for t in [0, 1, 2]:
    tess.forward(80)
    tess.left(120)
    
alex = turtle.Turtle()
alex.color('blue')
for a in [0, 1, 2, 3]:
    alex.forward(50)
    alex.left(90)

wn.mainloop()
