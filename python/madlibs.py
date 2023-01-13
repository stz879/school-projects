import time
import random

#startup
print("MadLibs v1.2")
print("Initializing...")
time.sleep(random.randint(1, 5))

def ask_for_story():
  print("Would you like to hear story 1 or story 2?")
  conf = int(input(""))
  if conf != 1 or 2:
    print("That is not a valid option.")
    ask_for_story();
 
ask_for_story()

#user prompts

print("Give me a NOUN")
noun = input("")

print("I need a PLURAL NOUN")
plural_noun1 = input("")
      
print("Try a PRESENT TENSE VERB")
present_tense_verb1 = input("")

print("Another PRESENT TENSE VERB?")
present_tense_verb2 = input("")

print("Alright, try a PLURAL PART OF THE BODY")
parts_of_body = input("")

print("An ADJECTIVE?")
adjective1 = input("")

print("A second PLURAL NOUN")
plural_noun2 = input("")

print("Final one! An ADJECTIVE")
adjective2 = input("")


#"wait time" - waits between 1 to 3 seconds
print("Generating story...")
time.sleep(random.randint(1, 3))
print("Alright, here it is:")
time.sleep(0.5)

#print story
if conf == 1:
  print(f"Today, every student has a computer small enough to fit into his {noun}.")
  print(f"He can solve any math problem by simply pushing the computer's little {plural_noun1}.")
  print(f"Computers can add, multiply, divide, and {present_tense_verb1}.")
  print(f"They can also {present_tense_verb2} better than a human.")
  print(f"Some computers are {parts_of_body}.")
  print(f"Others have a(n) {adjective1} screen that shows all kinds of {plural_noun2} and {adjective2} figures.")
elif conf == 2:
  print(f"I opened the door this morning and found a {noun} on my doorstep.")
  print(f"It didn't seem to have any name or note- but when I opened it up, there was {plural_noun1} inside.")
  print(f"I didn't see the person who left it, but I didn't want it to get stolen, so I had no choice but to {present_tense_verb1} it into the house.")
  print(f"I left it on the kitchen table and forgot about it... until it had {present_tense_verb2} on my {parts_of_body}.")
  print(f"")
else:
  time.sleep(1)
  print(f"Wait, this isn't right. You said you wanted story {conf}, but that isn't an option!")
  print("It's best you pick again.")
  ask_for_story();
