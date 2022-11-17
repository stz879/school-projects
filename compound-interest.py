import time
import random
import math

#choose between 1 to 3 seconds to wait while "calculating" later
sleepTime = random.randint(1, 5)

#define functions for use later
#used between years

#used if user is on the last year of saving
def finished():
    print('Type "Exit" to exit the program')
    inp = input("").strip().capitalize()
    if inp == "Exit":
        print("")
        print("Thank you for using the Compound Interest Program")
        print("")
    else:
        print("That is not a proper command")
        finished()
        


#prompt user
print("Hello! Welcome to the Compound Interest Program!")
print("Interest is 6% per year")
print("")
print("How much money will you deposit?")
#save deposit as a variable, and make it a float
depInput = input("")
dep = float(depInput)
#save number of years as a variable, and make it a float it too
print("How many years do you plan to leave it?")
yrsInput = input("")
yrs = int(yrsInput)


year1 = (dep * 0.06) + dep

i = 1
finalAmount = year1

while i < yrs:
    finalAmount = (year1 * 0.06) + year1
    i += 1



#added "load time" just for fun
print("Calculating...")
time.sleep(sleepTime)
print("Your total, after", yrs, "years, is $", '{:04.2f}'.format(finalAmount))
