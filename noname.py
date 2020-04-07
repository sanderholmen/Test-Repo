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
print('Type a number, please!')
myNumber = input()

try:
    if int(myNumber) > 5:
        print('Thats a high number!')
    else:
        print('Thats a low number!')
except ValueError:
    print('You did not type in a number!')
