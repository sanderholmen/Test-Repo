#This file is just a "sketching" file where I`ll write as I learn and move forward..


#A quick look at the "wihle-statement.

#Print out Hello, there! 5 times.
# testVar = 0
# while testVar < 5:
#     print('Hello, there!')
#     testVar = testVar + 1

# nameVariable = ''
# while True:
#     print('Your name, pls?')
#     nameVariable = input()
#     if nameVariable == 'Emil':
#         break #break statement causes the execution to immediatly leave the loop.
# print('Thanks!')


# randomVariable = 0
# while randomVariable < 5:
#     randomVariable = randomVariable +1
#     if randomVariable == 3:
#         continue # continue statement makes the computer jump back to the start of the while statement ignoring lines of code that would be after.
#     print('randomVariable is '+str(randomVariable))

# #Super simple and insecure login
# print('Please type in your username!')
# print('Hint: its "emil"!')
# usernameVariable1 = str(input())
# while usernameVariable1 != 'emil':
#     print('Wrong user! Please re-type your username!')
#     usernameVariable1 = str(input())
#     if usernameVariable1 == 'emil':
#         break
# print('Alrighty!')
# print('Now, type in your password!')
# print('Hint: it`s a quite common one..!')
# userPassword1 = str(input())
# while userPassword1 != '123':
#     print('Wrong, dude..!')
#     print('Try again!')
#     userPassword1 = str(input())
#     if userPassword1 == '123':
#         break
# print('You are now signed in, my friend!')

# #Looking at the "for" variable. with the "in range" function.
# print('I want apples!')
# for aWeirdVariable1 in range (5): #This will run the next code 5 times and each time its ran it will be adding an incremental values raning from 0-4 in the aWeirdVariable1.
#     if aWeirdVariable1 == 0: #We skip the first value as this is 0 and it does not make sense to the context. Notice the continue statement under.
#         continue #Here it is. Since the aWeirdVariable1 is valued at 0 at first, we chose to jump back to the start of the "for" statement.
#     print('I want ' + str(aWeirdVariable1))
# print('I want all apples!')


#Just looking at the for function and a usecase for it.
# #It basically just start with the number 0 and adds the sum of the 0 (aTotal1) + 0 and then, 1 and then 2... to 14 (addedToTotal1).
# aTotal1 = 0
# for addedToTotal1 in range (14):
#     aTotal1 = aTotal1 + addedToTotal1
# print(int(aTotal1))





# print('my name is..')
# randomVariable1 = 0
# while randomVariable1 < 5:
#     # if randomVariable1 == 0:
#     #     continue
#     print('Jeg teller ' + str(randomVariable1))
#     randomVariable1 = randomVariable1 + 1
# print('Ferdig')
# print('I want apples!')
# for aWeirdVariable1 in range (5): #This will run the next code 5 times and each time its ran it will be adding an incremental values raning from 0-4 in the aWeirdVariable1.
#     if aWeirdVariable1 == 0: #We skip the first value as this is 0 and it does not make sense to the context. Notice the continue statement under.
#         continue #Here it is. Since the aWeirdVariable1 is valued at 0 at first, we chose to jump back to the start of the "for" statement.
#     print('I want ' + str(aWeirdVariable1))
# print('I want all apples!')


# # print('Alrighty!')
# print('Now, type in your password!')
# print('Hint: it`s a quite common one..!')
# userPassword1 = str(input())
# while userPassword1 != '123':
#     print('Wrong, dude..!')
#     print('Try again!')
#     userPassword1 = str(input())
#     if userPassword1 == '123':
#         break
# print('You are now signed in, my friend!')
#

#You can write functions. Functions are defined (named) with the def statements.
#Inside a def statement youll write the code thats in the function. Remember to
#Have indentation (put a tab to move the lines of code in the "block").
# def hople():
#     print('hi')
#     print('How are you?')
#
# hople()
# hople()
# hople()

#
# #Taking a look at functions including while loop.
# def firstFunction():
#     if randomVariable2 == 1:
#         print('You typed "1"')
#     elif randomVariable2 == 2:
#         print('You typed "2"')
#     else:
#         print('You typed "3"')
#
# print('Type the number 1, 2 or 3!')
#
# randomVariable2 = int(input())
# if randomVariable2 == int(1) or randomVariable2 == int(2) or randomVariable2 == int(3):
#     firstFunction()
# else:
#     while randomVariable2 != int(1) or randomVariable2 != int(2) or randomVariable2 != int(3):
#         print('You did not type 1, 2 or 3!')
#         print('Please type 1, 2 or 3!')
#         randomVariable2 = int(input())
#         if randomVariable2 == int(1) or randomVariable2 == int(2) or randomVariable2 == int(3):
#             firstFunction()
#             break



# # Using a function in a simple math question to qoute the answer and using an if statement to decide which output to run.
# def secondFunction():
#     if randomVariable3 == int(4):
#         print('That is correct, ' + str(int(randomVariable3)) + ' is the answer!')
#     else:
#         print('No, ' + str(int(randomVariable3)) + ' is not the correct answer!')
#
#
# print('What is 2 + 2')
# randomVariable3 = int(input())
# if randomVariable3 == int(4): #You can see that both lines will be run, but the difference is the if statement inside "secondFunction"`s if statement.`
#     secondFunction()
# else:
#     secondFunction()



# #Calling a function with different argumetns.
# print('Type 1, 2 or any other number!')
# randomVariable4 = int(input())
#
# def thirdFunction(randomVariable4):# The word inside the parentheses is called a paramater. A parameter is a variable that an argument is stored in.
#     print('This ' +  randomVariable4)
#
# if randomVariable4 == int(1):
#     thirdFunction('parameter has a value of 1!')
# elif randomVariable4 == int(2):
#     thirdFunction('parameter has a value of 2!')
# else:
#     thirdFunction('parameter has a value of any other number you typed which in this case was ' + str(randomVariable4) + '!')


# #Handeling errors and examples of treating a function as a "black box" when all you want is the output of a function.
# def randomVariable5(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('No, dont divide by zero my friend!')
# #Since dividing by zero (notice the 3rd print statement) the program will output an error saying ZeroDivisionError: division by zero.
# #To overcome this so that the program can continue, you can add in "try and "except"" statements.
# print(randomVariable5(0))
# print(randomVariable5(1))
# print(randomVariable5(2))
# print(int(randomVariable5(3)))
# print(float(randomVariable5(5)))
# print(int(randomVariable5(21)))


#Taking another look at error handeling.
#This program fixes this by using the try and except statements.
# print('Type a number, please!')
# myNumber = input()
#
# try:
#     if int(myNumber) > 5:
#         print('Thats a high number!')
#     else:
#         print('Thats a low number!')
# except ValueError:
#     print('You did not type in a number!')


# #Using the random module to make a guessing game.
# import random #We import the random module..
# print('This is a guessing game!')
# secretVariable1 = random.randint(1, 20) #We set the variable "secretVariable1" to a random number between 1 and 20..
# print('Guess a number between 1 and 20!')
#
# for guessRemainingVariable in range(1, 7): #We set a range of 0 to 6 (not counting 7 as you remember) giving us 1 to 6 -> giving us 6 tries.
#                                            #This will run one line at a time in the for loop up to 6 times unless you guess correct.
#     print('Now, guess the number!')
#     guessVariable1 = int(input()) #We store the number that we guess as an integer in the "guessVariable1"..
#     if guessVariable1 < secretVariable1: #If number we guess is lower than the number that is random..
#         print('You have ' + str(int(6 - (guessRemainingVariable))) + ' tries left..!')
#         print('To low!')
#     elif guessVariable1 > secretVariable1: #If number that we guess is higher than the number that is random..
#         print('You have ' + str(int(6 - (guessRemainingVariable))) + ' tries left..!')
#         print('To high!')
#     else:
#         break #This condition would be met if your guess is correct. This takes us out of the "for" loop and move us on to the next block.
#
# if guessVariable1 == secretVariable1:
#     print('Your guess is correct, my friend. Congratulations!')
# else:
#     print('You ran out of tries, Im sorry. Good-bye!')




#Learning about the random function in python. A simple example usage would be a guessing game..
#I will also implement the "in range" function to limit the amount of tries the user have to guess the correct answer.
#Using the random module to make a guessing game would look something like this..
# import random #We import the random module..
# print('This is a guessing game!')
# secretVariable1 = random.randint(1, 20) #We set the variable "secretVariable1" to a random number between 1 and 20..
# print('Guess a number between 1 and 20!')
#
# for guessRemainingVariable in range(1, 7): #We set a range of 0 to 6 (not counting 7 as you remember) giving us 1 to 6 -> giving us 6 tries.
#                                            #This will run one line at a time in the for loop up to 6 times unless you guess correct.
#     print('Now, guess the number!')
#     guessVariable1 = int(input()) #We store the number that we guess as an integer in the "guessVariable1"..
#     if guessVariable1 < secretVariable1 and guessRemainingVariable <= 5: #If number we guess is lower than the number that is random and we have counted less than 0-5 (6 tries)..
#         print('You have ' + str(int(6 - (guessRemainingVariable))) + ' tries left..!')
#         print('To low, my friend, try again..!')
#     elif guessVariable1 > secretVariable1 and guessRemainingVariable <= 5: #If number that we guess is higher than the number that is random and we have counted less than 0-5 (6 tries)..
#         print('You have ' + str(int(6 - (guessRemainingVariable))) + ' tries left..!')
#         print('To high, my friend, try again..!')
#     else:
#         break #This condition would be met if your guess is correct. This takes us out of the "for" loop and move us on to the next block.
#
# if guessVariable1 == secretVariable1:
#     print('Your guess is correct, my friend. You used ' + str(int(guessVariable1)) + ' attempts. Congratulations!')
# else:
#     print('You ran out of tries. The number was ' + str(secretVariable1) + '.. Good-bye!')




#Lists are an important part of programming. As the program grows, storing values in lists becomes more important.
#Lets take a look at the list function.
listVariableOne = ['carrot', 'potato', 'lettuce'] #We are using square brackets to assign the values that are separated by commas in the list.
listVariableOne #Calling the listVariableOne will print out the whole list including the squarebrackets -> ['carrot', 'potato', 'lettuce'].
listVariableOne[1] #We are calling the listVariableOne and asking for the position 1 "index" (remember that it starts counting from 0). This means that 0 = carrot, 1 = potato and 2 = lettuce.

#We can also have lists containing lists. Lets take a look at lists of lists..
listVariableTwo = [['norway','sweden','denmark'],['oslo','stockholm','copenhagen']] #The syntax is basically [[','],[',']]
listVariableTwo #This will output: [['norway', 'sweden', 'denmark'], ['oslo', 'stockholm', 'copenhagen']]
listVariableTwo [0] #While this will output: ['norway', 'sweden', 'denmark']
listVariableTwo [0][2] #And this will output: 'denmark'
