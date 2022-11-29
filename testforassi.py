#CS195 - Assignment 5 - Janak
#program title
#Myname

from random import randint
myNum = randint(1,100)
guess_num = int(input("Guess a number between 1 and 100:"))
z = 0 #introducing a variable z which works as number of guessess 
while  guess_num != myNum:
      while guess_num<0:
         print ("Your guess should be more than 0.")
         z += 1
         guess_num = int(input("Guess a number between 1 and 100:"))
      else:
            #z = 0
         #guess_num = int(input("Guess a number between 1 and 100:"))
            if guess_num<myNum:
                  print("Your guess is too low. ")
                  z += 1
                  guess_num = int(input("Guess a number between 1 and 100:"))
            else:
                  z += 1
                  print ("Your guess is too high.")
                  guess_num = int(input("Guess a number between 1 and 100:"))
                 
                  #continue
else:
      print ("You won.") 
      print (f"Your score is {z}")
      
#continue
    
        
    