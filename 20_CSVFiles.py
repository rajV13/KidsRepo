# CSV files are files that stores comma separated values 
# Let's create a csv file containing names of countries and their capitals
# e.g. : India, New Delhi 
# and save that file with the name CountryList.csv
# To work with CSV files, we need to import the csv module

import csv

fileName = "CountryList.csv"
READ = "r"
READWRITE = "w+"

# Opening the file using "with open() as fileName :" syntax
# Reading the file using 'reader()' function which returns all the 
# rows of text in the file as a List

with open(fileName, mode=READ) as myFile:
    allRowsList = csv.reader(myFile)

    for currentRow in allRowsList:
        for country in currentRow:
            print(country + "  ", end="")
        print()

# There are few new things in the above code. 
# 'allRows' are the list of all the rows that were returned from a file
# 'currentRow' is the individual single rows from 'allRows'
# The single row in 'currentRow' contains [India, New Delhi]
# Again we used a loop to print the 2 items in the list
# New 'print(variableName, end="") -> to print in single line using loop

# We can use a delimiter to read the CSv files
# There are times when different symbols are used as delimiter
# We are using the delimiter "," as we have used the same in our csv file
print("\n\nReading a CSV File using delimiter\n")

with open(fileName, mode=READ) as myCSV:
    allRows = csv.reader(myCSV, delimiter=",")
    for currentRow in allRows:
        print(currentRow)

# So the optput contails the lists which kinda ungly looking. 
# So we can use 'print("delimiter".join(list))' to remove the brackets
# that are displayed and the " ' " on either side of the list items
# The following code will print a better formatted output

print("\n\nReading a CSV File and printing it with join\n")

with open(fileName, mode=READ) as myCSV:
    allRows = csv.reader(myCSV, delimiter=",")
    for currentRow in allRows:
        print("-->".join(currentRow))

print("\n\nRead Successful\n")