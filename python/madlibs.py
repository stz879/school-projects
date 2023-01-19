import time
import random

#startup
print("MadLibs v2.2")
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

def story_prompt():
  if conf == 1:
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
    
  elif conf == 2:
    print("Give me an ADJECTIVE")
    adjective1 = input("")
    
    print("Another ADJECTIVE?")
    adjective2 = input("")
    
    print("What about a TYPE OF FOOD?")
    food = input("")
    
    print("Alright, a ROOM IN A HOUSE (e.g. bathroom, bedroom, etc.)")
    room = input("")
    
    print("Now a PAST TENSE VERB")
    past_verb1 = input("")
    
    print("Ok, now a VERB")
    verb1 = input("")
    
    print("A person's NAME?")
    name = input("")
    
    print("Give me a NOUN")
    noun1 = input("")
    
    print("Now a LIQUID")
    liquid = input("")
    
    print("Now a VERB ENDING IN -ING")
    verb_ing1 = input("") 
    
    print("A plural PART OF THE BODY")
    part_of_body = input("")
    
    print("PLURAL NOUN?")
    plural_noun = input("")
    
    print("Give me another VERB ENDING IN -ING")
    verb_ing2 = input("")
    
    print("Last one! Give me a NOUN")
    noun2 = input("")
    
  else:
    time.sleep(1)
    print(f"Wait, this isn't right. You said you wanted story {conf}, but that isn't an option!")
    print("It's best you pick again.")
    ask_for_story();
    
    
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
  print(f"It was a {adjective1}, cold November day.")
  print(f"I woke up to the {adjective2} smell of {food} roasting in the {room} downstairs.")
  print(f"I {past_verb1} downstairs to see if I could help {verb1} the dinner.")
  print(f'My mom said, "See if {name} needs a fresh {noun1}."')
  print(f"So I carried a tray of glasses full of {liquid} into the {verb_ing1} room.")
  print(f"When I got there, I couldn't believe my {parts_of_body}!")
  print(f"There were {plural_noun} {verb_ing2} on the {noun2}!")
else:
  time.sleep(0.5)
  print(".")
  time.sleep(0.5)
  print(".")
  time.sleep(0.5)
  print(".")
  print(f"Wait, this isn't right. You said you wanted story {conf}, but that isn't an option!")
  print("It's best you pick again.")
  ask_for_story();
