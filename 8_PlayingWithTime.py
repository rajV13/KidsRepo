# We need to import the same datetime module 

import datetime

currentTime = datetime.datetime.now()

print(currentTime)
# The above line will print both date and time
# Separating components 
print()

print (currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

print()

# Printing only the time. For this we need the same 'strftime()' method

print (datetime.datetime.strftime(currentTime, "%I:%m:%S %p"))

# %H = hours (24-hours format)      %I (Capital i) = hours (12-hours format)       
# %m = minutes      %S = seconds    %p = AM or PM