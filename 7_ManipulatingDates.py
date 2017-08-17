# Python facilates the manipulation of dates with great ease ! 
# We can ask a user for his/her birthday and can manipulate it
# But there is a catch ! The input method returns a string 
# and we have to covert it into a DATE type
# The method 'strptime' helps us to convert a String into a Date

import datetime

userBirthday = input("Please enter your date of birth(mm/dd/yyyy) : ")
userBirthday = datetime.datetime.strptime(userBirthday, "%m/%d/%Y")
print(userBirthday.strftime("Your birth date is: %A %d %b %Y"))

# So why there is datetime.datetime? 
# This is because the 'strptime()' method is inside datetime class
# which is inturn inside the datetime module

# The 'strptime() return date along with time. To use the date from the datetime
# returned from the 'strptime(), we do something tlike this :

userBirthday = userBirthday.date()

# Arithmatic operations on dates ! See how easy it is to do in Pyhton
# Subtracting current date from birthday and we'll get the no. of days
# between the dates ! 

currentDate = datetime.date.today()
totalDays = currentDate - userBirthday

# To get the no. of days, we need to use the days property on totalDays like:
totalDays = totalDays.days

print()
print("So you're {0:d} days old" .format(totalDays))
print()

# Calculating approx age in years ! 
userAge = totalDays/ 365;

print("Which turnout to be {0:0.2f} years approx. !".format(userAge))
print()

# For more, look out for a dateutil module @ http://labix.org/python-dateutil