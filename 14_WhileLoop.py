# We mostly use while loops when we are not sure about the number of repeatations
# that has to be done.

answer = 0
counter = 1

while answer != 42 :
    answer = float(input ("What is the answer of life and universe?"))
    counter += 1  
print ("\nWell that's correct after {0:d} tries ! \n".format(counter))

import turtle 
print("Lets graw some graphics")
userSides = int(input("Enter the number of sides : "))
userColor = input("Enter the pen color : ")

turtle.color(userColor)
for steps in range (userSides):
    turtle.forward(50)
    turtle.right(360/userSides)
    for moreSteps in range (userSides):
        turtle.forward(30)
        turtle.right(360/userSides)