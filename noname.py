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


#Taking some more look at functions including while loop.
def firstFunction():
    if randomVariable2 == 1:
        print('You typed "1"')
    elif randomVariable2 == 2:
        print('You typed "2"')
    else:
        print('You typed "3"')

print('Type the number 1, 2 or 3!')
# randomVariable2 = int(input())
randomVariable2 = 'notasigned'
randomVariable2 = int(input())
if randomVariable2 == int(1) or randomVariable2 == int(2) or randomVariable2 == int(3):
    firstFunction()
else:
    while randomVariable2 != int(1) or randomVariable2 != int(2) or randomVariable2 != int(3):
        print('You did not type 1, 2 or 3!')
        print('Please type 1, 2 or 3!')
        randomVariable2 = int(input())
        if randomVariable2 == int(1) or randomVariable2 == int(2) or randomVariable2 == int(3):
            firstFunction()
            break
