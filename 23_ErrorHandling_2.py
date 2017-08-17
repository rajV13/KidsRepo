# let's try to grab the specific error and display a more proper 
# message to the user 

import sys

try :
    firstNumber = float(input("Enter first number: "))
    secondNumber = float(input("Enter second number: "))
    result = firstNumber/secondNumber
    print("{0:0.4f} / {1: 0.4f} = {2: 0.4f}".format(firstNumber, secondNumber, result))

except ZeroDivisionError : 
    print("\nAnything divided by 0 is infinity and beyond\n")

except : 
    print("\nSorry", sys.exc_info()[0], "occured")
 

finally :
    print("\nHave a nice day\n")
