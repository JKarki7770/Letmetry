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
    print("\033[H\033[2J", end="") #clear screen

    print (f'Your current health is {playerHealth}. You have {coins} coins and {len(myitems)} items. Your score is {score}.\n')

    print('Items available in the game:')
    for x in ITEMS:
        print(f'{x}    ', end='') #prints all the items in the tupple

    if len(myitems):
        print ('\nYour Items:')
        for y in myitems:
            print (f'{y}    ', end='')
    thing=  random.choice(ALL_THINGS) #choose something random for the player to encounter

    print (f'\n\nYou have encountered a {thing}.')
    

    if thing in ITEMS and thing not in myitems: 
            answer=input('Do you want this item?\n').lower()
            if answer!= "n":
                myitems+=(thing,)
                for z in myitems:
                    print (f' \n{z}'    , end='')
    elif thing in ITEMS and thing  in myitems: 
        print ('You already have this item.')
    elif thing in CREATURES:
        AttackAmount=7-len(myitems)
        print (f'The {thing} attacked you by an attack amount of {AttackAmount}. Your health is {playerHealth-AttackAmount}.')
        playerHealth-=AttackAmount
        if playerHealth<0:
            print ('You died.')
            exit
        playerResponse= input(f'Do you want to fight the {thing}?\n')
        if playerResponse.lower() != "n":
            if thing==CREATURES[0]:
                print (f'You defeated the {thing} and gained a score of 10.')
                score+=10
            elif thing!=CREATURES[0]:
                print (f'You defeated the {thing} and gained a score of 1.')
            score+=1
        if score>100:
            print ('You win this round. Congratulations.')
    input("\nPress ENTER to keep walking")