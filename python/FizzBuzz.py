print("Welcome to the FizzBuzz Program!")
print('What multiples should be "Fizz"?')
fizz_num = int(input(""))
print('What multiples should be "Buzz"?')
buzz_num = int(input(""))

#write numbers 1 - 100
for i in range(1, 101):
  fizz, buzz = False, False
    
  #check if divisible by 3, write to variable
  if i % fizz_num == 0: 
    fizz = True;

  #check if divisible by 5, write to variable
  if i % buzz_num == 0: 
    buzz = True;
  
#look at variables and output
  if fizz and buzz:
    print("FizzBuzz")
  elif fizz:
    print("Fizz")
  elif buzz:
    print("Buzz")
  else:
    print(i)
