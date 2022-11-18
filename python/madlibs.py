
import time
import random

#startup
print("MadLibs v0.01")
print("Initializing...")
time.sleep(random.randint(1, 5))

#user prompts
print("Give me an ADJECTIVE")
adj = input("")

print("Now give me a FOOD")
food = input("")

print("Past tense VERB?")
past_verb = input("")

print("What about a PERSON?")
person = input("")

print("Ok, now a RELATIVE")
relative = input("")

print("Give me a NOUN (singular)")
noun1 = input("")

print("Alright, now a LIQUID")
liquid = input("")

print("A VERB ending in -ING")
verb_ing = input("")

print("I need a NOUN (plural")
noun_plural = input("")

print("Last one! A piece of FURNITURE")
furniture = input("")

#"wait time" - waits between 1 to 3 seconds
print("Generating story...")
time.sleep(random.randint(1, 3))


#print story
print(f"It was a cold, {adj}, winter day.")
print(f"I woke up to the smell of {food} cooking downstairs.")
print(f"I {past_verb} down the stairs to help with the {food}.")
print(f"My {person} told me to see if my {relative} needed a fresh {noun1}.")
print(f"So I carried a tray of glasses full of {liquid} into the {verb_ing} room.")
print(f"When I came into the {verb_ing} room, I couldn't believe my eyes!")
print(f"There were {noun_plural} [verb_ing} on the {furniture}!")
