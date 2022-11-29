#CS195 - Assignment 5 - Janak
#program title

from random import randint


#define is used if the user want to play the game again.
def main():
    #generate a random number
    myNum= randint (1,100)
    
    while True:
        #get user response and ensure it's valid
        userinput=input("Guess a number between 1 and 100.\n")
        while not userinput.isdecimal():
            userinput=input("Your number is not valid. Please enter another number.\n")

        userinput=int(userinput) 

        if userinput<myNum:
            print("Your guess is too low. Please try again.\n")
        elif userinput>myNum:
            print("Your guess is too high. Please try again.\n")
        else:
            print(f" You won.")
            break

    reply=input("Do you want to play the game again?\n").lower()
    if reply==("yes"):
        main()
    else:
        exit()      
main()