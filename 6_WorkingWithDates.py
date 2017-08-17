# Date is also a data-type in python which helps us to mnipulate dates 
# We need to import the datetime module so that we can use date datatype
# Printing today's date using method/function today() which return today's date

import datetime

currentDate = datetime.date.today() 
print(currentDate)

# Printing the different parts of the date 
# The properties like year, month and day returns integers 
# Hence placeholders are required
print()
print ("Current year is : {0:d} ".format(currentDate.year))
print ("Current month is: {0:d} ".format(currentDate.month))
print ("Current day is  : {0:d} ".format(currentDate.day))
print()

# The numeric date can be often confusing to people of different palces 
# Therefore we must display the proper date format to avoid confusion
# There is a function 'strftime()' which allows us to specify the date format
# '%d' is for Day  '%b' is for Month '%Y' is for Year %A for name of the Day

print("Printing date using 'strftime()' function:")
print()
print (currentDate.strftime("%A %d %b %Y"))
print (currentDate.strftime("%b %A %d %Y"))
print (currentDate.strftime("%Y %A %d %b"))
print()

# Priting a date inside a sentace 
# Like "Today is Tuesday, Nov 17 and the year is 2015
print()
print("Printing the date inside a sentance and it's fun ! ")
print()
print(currentDate.strftime("Today is %A, %b %d and the year is %Y"))
print()

# For localizing dates and currencies so that it will be valid for each country then 
# look out for the Python babel library http://babel.pocoo.org