# Intro to Turtle ! 
# A graphic drawer 
# Functions in Turtle are :
# right(x)        -> move cursor right by x degrees
# left(x)         -> move cursor left by x degrees
# forward(x)      -> draw a line x pixels long
# backward(x)     -> draw a line x pilexs long backward
# color("x")      -> changes the color of the RecursionError/pen

# Drawing a square using turtle ! 

import turtle

turtle.color("yellow")
turtle.forward(100)
turtle.right(90)
turtle.color("green")
turtle.forward(100)
turtle.right(90)
turtle.color("red")
turtle.forward(100)
turtle.right(90)
turtle.color("blue")
turtle.forward(100)

# As we can see, there is lots of repeatation of the same line of code ! 
# In such cases, we use loops to repeat the tast or same lines of codes
# We mostly use for loop when we kow the number of repeatations that are to be done

for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
    turtle.color("red")

    for steps in range(4):
        turtle.forward(50)
        turtle.right(90)
        turtle.color("green")
        for steps in range(4):
            turtle.forward(25)
            turtle.right(90)

print ("That's all folk")