# In this application, we'll just ask the user for the names of their friends 
# and store it in a list and display the final list containing all the names

listOfFriends = []
inputName = ""
counter = 0

print ("Enter the names of your friends [Enter 'X' to stop] \n")

while inputName != "X" and inputName != "x":
    inputName = input("Enter friend's name : ")
    listOfFriends.append(inputName)

# Printing the list 
print("\n\nHere is the list of your friends: \n")
for names in listOfFriends:
    if names != "" and names != "X" and names != "x":
        print(names)

print ("\nBye !")