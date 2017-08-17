# Lists are like dynamic arrays in Python
# Can contain heterogenous data nut it is advisable to keep 
# homogeneous data items in a list

myCountryList = ["India", "USA", "Japan", "Australia"]

# Using append() method to add item in the list
# append() method add the items/values to the end of the list
myCountryList.append("Canada")
myCountryList.append("Russia")
print (myCountryList)

# Overwriting value of an item in the list using index
myCountryList[3] = "XYZ"
print(myCountryList)

# We can print the latest addition to the list by printing th -1 index
print(myCountryList[-1])

# We can print the value from backwards using -ve index numbers
# if you want the last item just use [-1] as index
# same with second last [-2], third last [-3] and so on....
print (myCountryList[-3])

# Using del command to delete a value on a particular index
del myCountryList[1]

print (myCountryList)
myCountryList.append("USA")

# Deleting item using the remove() method
myCountryList.remove ("Japan")
print(myCountryList)

# We can print the index of a value in the list 
print (myCountryList.index("USA"))

# Lets check for the index of a value which is not inside the list
#print(myCountryList.index("ZZZ"))
# We'l get an error in this case which can be solved using error handling.

print("\nPrinting list before sorting")
print(myCountryList)

# Sorting a list in alphabatical order
print("\nPrinting a list after sorting it")
myCountryList.sort()
print(myCountryList)

#Reverse sorting a list using 'reverse()' method
print("\nReversing the list :")
myCountryList.reverse()
print(myCountryList)

# Printing the values in a list using for loop 
print("\nPrinting list using for-loop")
for names in myCountryList:
    print (names)

# Printing values in the list using while loop
# We can get the lengtht of the list using 'len()' method
# which accepts the list as a parameter

print("\nprinting list using while loop")
lengthOfList = len(myCountryList)
counter = 0
print()

while counter < lengthOfList :
    print(myCountryList[counter])
    counter += 1

print("\nThat's all folk ! Have fun with lists.")