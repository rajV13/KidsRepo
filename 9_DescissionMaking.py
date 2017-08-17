userAnswer = input("Are you hungry? ")

# Single condition checking
if userAnswer.lower() == "yes" :            
    print("In that case you should cook something :-P\n")
else :
    print("It's ok then, go back to work\n")
print("Well now if you're not hungry, then..\n")

userWork = input("Can you work now?")

# Multiple condition in a single if statement
if userWork.lower() == "yes" or userWork.lower() == "y" : 
    print("It's good, you are very active person")
else :
    print("You are so lazy, get a cup of coffee")

# Best practice 
# Save your expected answer in a variable and convert them in the same case
# before comparing

userAnswer = input("\nHave you finished your work?")
expectedAnswer = "yes"
expectedAnswer = expectedAnswer.lower()

if userAnswer == expectedAnswer : 
    print("Well done. Take rest\n")
else :
    print("Finish it fast\n")
print("Have a nice day\n")