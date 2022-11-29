#CS195 - Assignment 5 - Janak
#program title

from random import randint
    #generate a random number
myNum= randint (1,100)
z=0 #Z IS NUMBER OF TRIES.

while True:
    #get user response and ensure it's valid

    userinput=input("Guess a number between 1 and 100.\n")
    while not userinput.isdecimal():
        userinput=input("Your number is not valid. Please enter another number.\n")

    userinput=int(userinput) 

    if userinput<myNum:
        print("Your guess is too low. Please try again.\n")
        z+=1
    elif userinput>myNum:
        print("Your guess is too high. Please try again.\n")
        z+=1
    else:
        z+=1
        #z is number of tries the user made
        print(f" You won. Your score is  {10 - z} ")
        break



