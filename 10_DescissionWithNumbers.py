# Since the user input is always string, we need to convert it
# into float or integer for doing calculations on it. 

bonus = 0
extraBonus = False
deposit = float(input("Enter the amount you want to deposit: "))


if deposit > 500 : 
    bonus = 50
else :
    bonus = 20
finalDeposit = deposit + bonus

if finalDeposit > 1000 :
    extraBonus = True

if extraBonus : 
    finalDeposit += 80
    print ("\nYou have got extra bonus !!")

print("Your saving has Rs.{0:0.2f}".format(finalDeposit))