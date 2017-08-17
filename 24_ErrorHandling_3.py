# A more better program. Lets check for the errors in the input numbers
# This program keeps looping until the user provide correct inputs
import sys

while True:    # Infinite loop
    try :
        # In case of erroe in mismatched value, the control will
        # transfer to the "except ValueError :" block
        firstnum = float(input("Enter fitst number: "))
        secondNum = float(input("Enter another number: "))
        
        # Incase of error in calculation of result, like division with 0,
        # the control will transfer to the "except ZeroDivisionError :" block.
        result = firstnum/secondNum

        break; # Break will only be executed when there is no error

    except ValueError : 
        print("\nThat was not a valid input. Please try again")

    except ZeroDivisionError :
        print("\nAnything divided by 0 is infinity !")
        
    except : 
        print ("\nSomething is wrong. Try Again! ")
    
print(result)
print("\nHave a nice day\n")