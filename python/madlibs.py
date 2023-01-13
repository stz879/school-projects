import time
import random

#startup
print("MadLibs v1.2")
print("Initializing...")
time.sleep(random.randint(1, 5))

print("Would you like to hear story 1 or story 2?")
conf = int(input(""))

if conf == 1:
  global story
  story

#user prompts
print("Give me an ADJECTIVE")
adjective = input("")

print("Now give me a NOUN")
first_noun = input("")

print("Past tense VERB?")
past_tense_verb = input("")

print("What about a PERSON?")
person = input("")

print("Ok, now a RELATIVE")
relative = input("")

print("Give me a NOUN")
second_noun = input("")

print("Alright, now a NOUN")
third_noun = input("")

print("Can you think of a VERB?")
verb = input("")

print("I need a PLURAL NOUN")
plural_noun = input("")

print("A fourth NOUN")
fourth_noun = input("")

print("Last one! Another VERB")
second_verb = input("")

#"wait time" - waits between 1 to 3 seconds
print("Generating story...")
time.sleep(random.randint(1, 3))


#print story
print(f"It was a cold, {adjective}, winter day.")
print(f"I woke up to the smell of {first_noun} cooking downstairs.")
print(f"I {past_tense_verb} down the stairs to help with the {first_noun}.")
print(f"My {person} told me to see if my {relative} needed a fresh {second_noun}.")
print(f"So I carried a tray of glasses full of {third_noun} into the {verb}ing room.")
print(f"When I came into the {verb}ing room, I couldn't believe my eyes!")
print(f"There were {plural_noun} {second_verb}ing on the {fourth_noun}!")

