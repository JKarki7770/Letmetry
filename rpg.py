
#CS195 - Assignment 6 - Janak
#Text based rpg game

import random


CREATURES= ('monster','rabbit','fox','rat')
ITEMS= ('helmet','shield', 'boots', 'chest plate', 'gauntlets')
OTHER_THINGS= ('bush', 'big tree', 'rock')
ALL_THINGS= (CREATURES+ITEMS+OTHER_THINGS)

myitems= ()
playerHealth= 20 
coins = 100
score= 0

while True: 
    #clear screen
    print("\033[H\033[2J", end="") 
    print (f'current health = {playerHealth}.       coins = {coins}     Number of items = {len(myitems)}       score =  {score}.\n')

    print('Items in this game:')
    for x in ITEMS:
        print(f'{x}    ', end='') 
        #showing users the item they have

    if len(myitems):
        print ('Your Items:\n')
        for y in myitems:
            print (f'{y}    ', end='')
    rthing=  random.choice(ALL_THINGS) 
    #Player encounter random things

    print (f'\n\nYou have encountered a {rthing}.')
    

    if rthing in ITEMS and rthing not in myitems: 
            answer=input('Do you want this item?\n').lower()
            if answer!= "n":
                myitems+=(rthing)
                for z in myitems:
                    print (f' your items:\n{z}'    , end='')
    elif rthing in ITEMS and rthing  in myitems: 
        print ('You already have this item.')
    elif rthing in CREATURES:
        AttackAmount=7-len(myitems)
        print (f'The {rthing} attacked you by an attack amount of {AttackAmount}. Your health is {playerHealth-AttackAmount}.')
        playerHealth-=AttackAmount
        if playerHealth<=0:
            print ('You died.')
            exit
        playerResponse= input(f'Do you want to fight the {rthing}?\n')
        if playerResponse.lower() != "n":
            if rthing==CREATURES[0]: #used index 0 so if it is monster the user gets 10 points.
                print (f'You killed the {rthing} and gained a score of 10.')
                score+=10
            elif rthing!=CREATURES[0]:
                print (f'You killed the {rthing} and gained a score of 1.')
            score+=1
        if score>100:
            print ('You won this round. Congratulations.')
    input("\nPress ENTER to keep walking")

