# in Python, we have to define a function before we can use it. 
# def keyword is used to define a function followed by th neme of the function
# and then the parameters
# The main() function is called at the bottom

def main():
    fileName = "CountryList.csv"
    myList = ["C", "Python", "Java", "C++", "NodeJS", "JavaScript"]

    printListSL (myList)
    printList (myList)
    print()
    value = printFile(fileName)
    printFileLineByLine(fileName)
    print(value)
    print("-----------\nWell it works")
    return


# Function to print the contents of a file
def printFile(fileName):
    print ("Priting the contents of a file:\n")
    myFile = open(fileName, mode="r")
    fileData = myFile.read()
    print(fileData)
    print("--------------\n")
    myFile.close()
    return


# Function to print the contents of a file line by line
# You can notice a line gap because this function will print '\n' as well
def printFileLineByLine(fileName):
    print ("Priting the contents of a file line by line:\n")
    myFile = open(fileName, mode="r")
    for lines in myFile:
        print(lines)
    myFile.close()
    return


# Function to print a list in a single line
def printListSL (list):
    print("Printing the list item in a line...\n")
    for items in list:
        print(items + "  ", end="")
    print("\n")
    return


# Function to print a list line by line
def printList (list):
    print("Printing the list items...\n")
    for items in list:
        print(items)
    print("\n")
    return


# Calling the main() function
main()
# There was no need of the main function but it makes the code a bit clean
