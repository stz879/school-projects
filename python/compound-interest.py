import time
import random
import math


#prompt user
print("Hello! Welcome to the Compound Interest Program!")
time.sleep(1)
print("")
print("")
print("How much interest? (as a decimal, ex 0.06 = 6%")
interest = float(input(""))
print("How much money will you deposit?")
#save deposit as a variable, and make it a float
depInput = input("")
dep = float(depInput)
#save number of years as a variable, and make it a float it too
print("How many years do you plan to leave it?")
yrsInput = input("")
yrs = int(yrsInput)

#calculate 1st year. done for variable convenience
year1 = (dep * interest) + dep

i = 1
finalAmount = year1

#loop for each year
while i < yrs:
    finalAmount = (finalAmount * interest) + finalAmount
    i += 1
    print(f"Year {i}")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("How much money would you like to add to your deposit?")
    print("Type 0 if you don't want to add any more money")
    x = input("")
    float(x)
    finalAmount += x



#added "load time" just for fun
print("Calculating...")
time.sleep(random.randint(1, 3))
#                                                v make the end result at least 4 characters, with 2 numbers past the decimal point
print(f"Your total, after {yrs} years, is $", '{:01.2f}'.format(finalAmount))
