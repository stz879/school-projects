
import time
import random

#user prompt
print("Give me an ADJECTIVE")
adj1 = input("")
print("Now give me a FOOD")
food = input("")


print("Generating story...")
time.sleep(random.randint(1, 3))

print("It was a cold,", adj1, ", winter day. I woke up to the smell of", food, "cooking downstairs.")
