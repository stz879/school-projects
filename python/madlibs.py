
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
print("Ok, now a RELATIVE")
relative = input("")
print("Give me a NOUN!")
noun1 = input("")

print("Generating story...")
time.sleep(random.randint(1, 3))

print("It was a cold,", adj, ", winter day.")
print("I woke up to the smell of", food, "cooking downstairs.")
print("I", past_verb, "down the stairs to help with the", food, ".")
print("My", person, "told me to see if my", relative, "needed a fresh", noun1)
