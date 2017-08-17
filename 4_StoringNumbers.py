# This program shows how we can store numbers in our code in Python !

# There is a special operators in Python. 
# ' ** ' is for exponent       e.g: 2**3 = 8
# i.e 2 to the power of 3

print ("")
numOne = 5  
power  = 4  
result = numOne**power;

# Most simple way to print number is :
print("First Method  : The result is", result)

# Placeholders in python for printing numbers
# Old style placeholder
print ("Second method : The result is %d" %result)

# New addition in python 3
print ("Third Method  : The result is {0:d}".format(result))

# Printing more than 1 numbers in {} or .format() style
# The {} placeholde takes 2 parameters 
# {position of num : type of num}
# if we want to print 3 nums say 5, 6, 7 then position will be 0, 1 and 2
# for decimal, type is d, float f and so on...

print("\nNow printing more than 1 nums in a single line using .format()")
 
# so if we want to print 5, 6, 7 is a single line then we will do it like this: 

print ("1st is: {0:d} 2nd is: {1:4d} 3rd is: {2:06d}".format(5, 6, 7))

# using a num before data type sepecifies width of the digit, 
# generally used for formatting of output 
# using '0' before data type replaces spaces with digit 0

print()