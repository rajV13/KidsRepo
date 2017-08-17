import sys

firstNumber = float(input("Enter 1st number : "))
secondnumber = float(input("Enter 2nd number : "))


try :
    result = firstNumber / secondnumber
    print("\n"+ str(firstNumber) +"/"+ str(secondnumber) +" = "+ str(result))

except:
    error = sys.exc_info()[0]
    print("\nSomething is wiered. Try Again! ")
    print(error)

finally:
    print("\nHave a nice day\n")