
import time
import random

#user prompt
print("Give me an ADJECTIVE")
adj = input("")
print("Now give me a FOOD")
food = input("")
print("Past tense VERB?")
past_verb = input()
print("What about a PERSON?")
person = input("")

print("Generating story...")
time.sleep(random.randint(1, 3))

print("It was a cold,", adj, ", winter day."
"I woke up to the smell of", food, "cooking downstairs."
"I", past_verb, "down the stairs to help with the", food, "."
"My", person, )
