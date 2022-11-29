import random
CREATURES = 'monster', 'rabbit', 'fox', 'rat'
ITEMS = 'helmet', 'shield', 'boots', 'chest plate', 'gauntlets'
OTHER_THINGS = 'bush', 'big tree', 'rock'
ALL_THINGS = CREATURES + ITEMS + OTHER_THINGS
random.choice(ALL_THINGS)
print (ALL_THINGS)
#value = ALL_THINGS.randint
value = random.choice(ALL_THINGS)
print (value)   
if value == rabbit:
    curious = input("Do you wanna fight?")
    if curious == "yes".lower():
        print("Sorry You lost")
    else:
        print ("You escaped.")

else:
    print ("IThis could be an item. Do you want to take it?")

