    #Learning about the random function in python. A simple example usage would be a guessing game..
#I will also implement the "in range" function to limit the amount of tries the user have to guess the correct answer.
#Using the random module to make a guessing game would look something like this..
import random #We import the random module..
print('This is a guessing game!')
secretVariable1 = random.randint(1, 20) #We set the variable "secretVariable1" to a random number between 1 and 20..
print('Guess a number between 1 and 20!')

for guessRemainingVariable in range(1, 7): #We set a range of 0 to 6 (not counting 7 as you remember) giving us 1 to 6 -> giving us 6 tries.
                                           #This will run one line at a time in the for loop up to 6 times unless you guess correct.
    print('Now, guess the number!')
    guessVariable1 = int(input()) #We store the number that we guess as an integer in the "guessVariable1"..
    if guessVariable1 < secretVariable1 and guessRemainingVariable <= 5: #If number we guess is lower than the number that is random and we have counted less than 0-5 (6 tries)..
        print('You have ' + str(int(6 - (guessRemainingVariable))) + ' tries left..!')
        print('To low, my friend, try again..!')
    elif guessVariable1 > secretVariable1 and guessRemainingVariable <= 5: #If number that we guess is higher than the number that is random and we have counted less than 0-5 (6 tries)..
        print('You have ' + str(int(6 - (guessRemainingVariable))) + ' tries left..!')
        print('To high, my friend, try again..!')
    else:
        break #This condition would be met if your guess is correct. This takes us out of the "for" loop and move us on to the next block.

if guessVariable1 == secretVariable1:
    print('Your guess is correct, my friend. You used ' + str(int(guessVariable1)) + ' attempts. Congratulations!')
else:
    print('You ran out of tries. The number was ' + str(secretVariable1) + '.. Good-bye!')
