# To read a file we have to open it in reading mode 
fileName = "DemoReadFile.txt"
READ = "r"

myFile = open(fileName, mode=READ)

# Reading from the file (All the content at once )
fileContent = myFile.read()
print (fileContent)
myFile.close()
print ("\n\nFile read Successful. \n")


# Reading a line at once 
myFile = open(fileName, mode=READ)
line = myFile.readline()
print(line)
myFile.close()

print ("\n\nFile read Successful !\n")
print("Now reading a file line by line")
print("--------------------------------\n")

# Using loop to read from a file line by line 

myFile = open(fileName, mode=READ);
for lines in myFile:
    print(lines)
myFile.close()
print()

# Another way to open file where python will automatically 
# handle exceptions/errors and will close the file
print("Again reading a file line by line using 'with open() as' syntax")
print("--------------------------------\n")

with open(fileName, mode=READ) as myFile:
    # Reading line by line 
    for lines in myFile:
        print(lines)

print("\nThat's all for now ! \n") 