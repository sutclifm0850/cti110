#P4LAB
#Nested Loops
#SUTCLIFFE
#March 25, 2018

import turtle
wn = turtle.Screen()
wn.bgcolor('gray')
mary = turtle.Turtle()

mary.color('turquoise')
mary.pensize(5)
mary.shape('turtle')

for a in(1,2,3,4,5):
    for b in(1,2,3):
        mary.forward(100)
        mary.left(120)
    mary.forward(100)
    mary.right(72)

wn.mainloop()
