#Functions are an important part of programming. Regardless of language, you will see this as a core part of software developement.

#Looking at the "for x in range" function.
print('I want apples!')
for aWeirdVariable1 in range (5): #This will run the next code 5 times and each time its ran it will be adding an incremental values raning from 0-4 in the aWeirdVariable1.
    if aWeirdVariable1 == 0: #We skip the first value as this is 0 and it does not make sense to the context. Notice the continue statement under.
        continue #Here it is. Since the aWeirdVariable1 is valued at 0 at first, we chose to jump back to the start of the "for" statement.
    print('I want ' + str(aWeirdVariable1))
print('I want all apples!')


#Just looking at the for function and a usecase for it.
#It basically just start with the number 0 and adds the sum of the 0 (aTotal1) + 0 and then, 1 and then 2... to 13
#(counting from 0 to 13 = 14) (addedToTotal1).
aTotal1 = 0
for addedToTotal1 in range (14):
    aTotal1 = aTotal1 + addedToTotal1
print(int(aTotal1))


#Taking a look at functions including while loop.
def firstFunction():
    if randomVariable2 == 1:
        print('You typed "1"')
    elif randomVariable2 == 2:
        print('You typed "2"')
    else:
        print('You typed "3"')

print('Type the number 1, 2 or 3!')

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


# Using a function in a simple math question to qoute the answer and using an if statement to decide which output to run.
def secondFunction():
    if randomVariable3 == int(4):
        print('That is correct, ' + str(int(randomVariable3)) + ' is the answer!')
    else:
        print('No, ' + str(int(randomVariable3)) + ' is not the correct answer!')


print('What is 2 + 2')
randomVariable3 = int(input())
if randomVariable3 == int(4): #You can see that both lines will be run, but the difference is the if statement inside "secondFunction"`s if statement.`
    secondFunction()
else:
    secondFunction()



#Calling a function with different argumetns.
print('Type 1, 2 or any other number!')
randomVariable4 = int(input())

def thirdFunction(randomVariable4):# The word inside the parentheses is called a paramater. A parameter is a variable that an argument is stored in.
    print('This ' +  randomVariable4)

if randomVariable4 == int(1):
    thirdFunction('parameter has a value of 1!')
elif randomVariable4 == int(2):
    thirdFunction('parameter has a value of 2!')
else:
    thirdFunction('parameter has a value of any other number you typed which in this case was ' + str(randomVariable4) + '!')
