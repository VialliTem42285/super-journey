import random
def guess(x):
             random_number = random.randint(1,10)
             guess = 0
while guess != random_number:
     
 guess = int( input("Enter a guess between 1 to 10: "))

                                if guess < random_number:
                                                       print ("Too low, guesss again")
                                 elif guess > random_number:
                                                         print ("Too high, guess again")
                

print ('Yay, congrats, you have guessed the right number  {}')

guess(10)
