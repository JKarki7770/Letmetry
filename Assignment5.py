#CS195 - Assignment 2 - Janak
#program title
#Myname

from random import randint
myNum = randint(1,100)
guess_num = int(input("Guess a number between 1 and 100:"))
#if guess_num<0:
       #print ("Enter positive number")
       #print ("Your guess should be more than 0.")
       #guess_num = int(input("Guess a number between 1 and 100:"))

while  guess_num != myNum:
      while guess_num<0:
         print ("Your guess should be more than 0.")
         z = 0
         z += 1
         guess_num = int(input("Guess a number between 1 and 100:"))
      else:
            z = 0
         #guess_num = int(input("Guess a number between 1 and 100:"))
            if guess_num<myNum:
                  print("Your guess is too low. ")
                  x = 0
                  x += 1
                  guess_num = int(input("Guess a number between 1 and 100:"))
            else:
                  x = 0
                  print ("Your guess is too high.")
                  y = 0
                  y += 1
                  guess_num = int(input("Guess a number between 1 and 100:"))
                 
                  #continue
else:
      y = 0
      print ("You won.") 
      m= x+y+z
      J = 10 - m
      print (f"Your score is {10-m}")
#continue
    
        
    