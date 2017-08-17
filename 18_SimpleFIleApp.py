# This file will store the list of friends into a file 
# that can be used to read the list even when the program is not running 
myFriendList = []
counter = 0
userInput = ""
fileName = "ListOfFriends.csv"
APPEND = "a"

print("Please enter the the names of your friends" +\
      "[Enter X to stop]")

# The above is an example of concatenating text 
# if it is too long for your display resolution. 
# Ofcourse word wrap can also do this task. 
# Let's create a list ! 

while userInput != "X" and userInput != "x":
    userInput = input("Enter the name of your friend : ")
    if userInput != "" and userInput != "X" and userInput != "x":
        myFriendList.append(userInput)

numberOfFriends = len(myFriendList);
print ("\nTotal number of friends is : {0:d}\n".format(numberOfFriends))

#Just to see everything going well. 
#for names in myFriendList:
#    print(names)

myFile = open(fileName, mode=APPEND)

for names in myFriendList:
    myFile.write(names + "'\n")

myFile.close()

print("\nFile '"+ fileName + "' written successfully\n")