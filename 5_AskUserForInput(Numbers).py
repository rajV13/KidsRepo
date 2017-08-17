# By default, the input is a string in Python.
# We have to convert it into a number. 
# There are functions which convert one datatype to another datatype

salary = input("Please enter your salary: ")
bonus = input("Please enter the bonus amount you want: ")

payCheckAmount = float(salary) + float(bonus)

print("Your Cheque amount is {0:0.2f}".format(payCheckAmount))

# The user can also enter strings instead of numbers. 
# So we need exception handling for that situation 
# and prevent the program from crashing. 