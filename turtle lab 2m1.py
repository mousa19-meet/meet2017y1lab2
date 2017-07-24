import turtle

# Everything that comes after the # is a

# comment.

# It is a note to the person reading the code.

# The computer ignores it.

# Write your code below here...
turtle.penup() #Pick up the pen so it doesn’t

#draw

turtle.goto(-200,-100) #Move the turtle to the

#position (-200, -100)

#on the screen

turtle.pendown() #Put the pen down to start

#drawing

#Draw the M:

turtle.goto(-200,-100+200)

turtle.goto(-200+50,-100)

turtle.goto(-200+100,-100+200)

turtle.goto(-200+100,-100)
#draw E
turtle.penup()


turtle.goto(0,100)
turtle.pendown()
turtle.goto(0,-200+100)
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.goto(0,100)
turtle.pendown()
turtle.penup()
turtle.goto(0,10)
turtle.pendown()
turtle.goto(100,10)
turtle.goto(0,10)
# ...and end it before the next line.

turtle.mainloop()
