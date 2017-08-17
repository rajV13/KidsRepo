# We use the 'open()' method to open and write to a file
# open(fileName, mode=accessMode )
# The different modes for opening a file are :
# 'r'   -> reading mode
# 'w'   -> writing mode (overwrite old data)
# 'a'   -> append mode (add next to the old data)
# 'w+'  -> read and write mode 
# 'b'   -> open binary files like video, images, etc

fileName = "DemoWriteFile.txt"
# accessMode = "w"
# Lets try a more readable variable name
WRITE = "w" 
APPEND = "a"
READWRITE = "w+"

# myFile = open(fileName, accessMode)
myFile = open(fileName, mode=READWRITE)

# Using the method 'write()' to write to the file.

myFile.write ("This is a demo text. ")
myFile.write ("Ohh..that's in the same line")
myFile.write ("\n\nThis will be in a new line ")

# We must close the file after writing into it.
myFile.close()

print("File Written...Bye!")