#CS195 - Assignment 6 - Janak
#Text based rpg game

import random


CREATURES= ('monster','rabbit','fox','rat')
ITEMS= ('helmet','shield', 'boots', 'chest plate', 'gauntlets')
OTHER_THINGS= ('bush', 'big tree', 'rock')
ALL_THINGS= (CREATURES+ITEMS+OTHER_THINGS)

playerHealth= 20 
items= ()
coins = 100
score= 0

while True:
    print("\033[H\033[2J", end="") 
    print(f"Current health = {playerHealth}. score= {score}.   ")
    


