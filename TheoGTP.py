###TheoGTP###

import random
import time

number_of_conversations = 0


# moods

#Greetings

startled_greeting = ["HUH" , "Excuse me young lady?" , "AHDFGHD DGFHDGFHAFHEVBAV EHHDAYG"]
regular_greeting = ["Hello" , "Yes?" , "Hold on ... yeah?"]
angry_greeting = ["no","shut up"]
idle = ["HEHEHEHA","Screw you","ALLLLLLLrigh then","My arrows are very effective charlie"]



def conversation(startled):
    global startled_greeting , regular_greeting , angry_greeting
    while True:

        user_input = input(">>")

        if startled == True and greeting != True and "hi" not in user_input.lower() :
            x = random.randint(0,(len(startled_greeting)-1))
            print(f"Theo>>{startled_greeting[x]}")
            greeting = True
        elif greeting != True:
            x = random.randint(0,(len(regular_greeting)-1))
            print(f"Theo>> {regular_greeting[x]}")
            greeting = True
        
        elif "goodbye" in user_input.lower():
            print("Bye")
            break

        
        if "leave" in user_input.lower() or "exit" in user_input.lower():
            print("Theo>> Well you have to say goodbye, obviously")
            print("Theo>> Would be rude not to")

        if "67" in user_input:
            break

        if user_input == "":
            x = random.randint(0,(len(idle)-1))
            print(f"Theo>> {idle[x]}")

        if user_input != "":
            print("Thats beyond my capabilities at the moment")
        


        

def patches_and_rules():
    print("Current version: 1.2")

    print("####################")
    print("Rules:")
    print("To end coversation say goodbye")
    print("")

    print("####################")
    print("Version Notes")
    print("Disgusted by 67")
    print("tells you how to leave when asked")
    print("idle voice lines")
def sys_loop():
    global number_of_conversations
    number_of_conversations = number_of_conversations + 1
    if number_of_conversations <= 3:
        startled = True
    else:
        startled = False

    while True:
        print("# 1. Start conversation")
        print("# 2. View version Logs")

        x = input()

        try:
            int(x)
        except:
            print("error")
        else:
            break

    if x == "1":
        conversation(startled)
    if x == "2":
        patches_and_rules()


while True:
    sys_loop()