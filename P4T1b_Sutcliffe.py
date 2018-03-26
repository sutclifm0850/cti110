#P4T1b
#Initials
#Sutcliffe
#March 23, 2018

import turtle
wn = turtle.Screen()
wn.bgcolor('gray')
mary = turtle.Turtle()
mary.color('turquoise')
mary.pensize(5)

mary.left(90)
mary.forward(120)
mary.right(160)
mary.forward(60)
mary.left(140)
mary.forward(60)
mary.right(160)
mary.forward(120)

mary.up()
mary.left(90)
mary.forward (50)
mary.down()

for s in [0, 1]:
 mary.forward(60)
 mary.left(90)
for s in [0, 1, 2]:
 mary.forward(60)
 mary.right(90)

wn.mainloop()

        
