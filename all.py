#My first lines of code which are ofc quite uninteresting.
print('Hello, Lets start off with you')

print('What is your name?') #This asks for name..
nameVariable = input() #set variable for name that you type
print('It is good to meet you, ' + nameVariable)
print('The length of your name is:')
print(len(nameVariable))   #len is a function that counts letters

print('What is your age?') #Ask for age..
ageVariable = input() #set variable for age that you tyoe
print('You will be ' + str(int(ageVariable) + 1) + ' in a year.')


#break and continue statement examples..
nameVariable = ''
while True:
    print('Type your name, pls. Only Emil is granted?')
    nameVariable = input()
    if nameVariable == 'Emil':
        break #break statement causes the execution to immediatly leave the loop.
print('Thanks!')

randomVariable = 0
while randomVariable < 5:
    randomVariable = randomVariable +1
    if randomVariable == 3:
        continue # continue statement makes the computer jump back to the start of the while statement ignoring lines of code that would be after.
    print('randomVariable is '+str(randomVariable))


#What is 2+2 my simple math question the sophisticated version.
print('Hello, can you type you`r name in for me please?!')
nameVar = ('')
while nameVar != bool(0):
	#while nameVar != str(''):
	nameVar = str(input())
	#print('Thanks, ' + nameVar + '!')
	break
print('Good to meet you, ' + nameVar + '!')
theCorrectAnswer = 2 + 2
print('what is 2+2?')
myAnswer = int(input())
if theCorrectAnswer == myAnswer:
	print('Correct!')
elif theCorrectAnswer == myAnswer + 1 or theCorrectAnswer == myAnswer - 1:
    print('You are close, try again!')
    while theCorrectAnswer == myAnswer + 1 or theCorrectAnswer == myAnswer - 1:
        my2ndAnswer = int(input())
        if theCorrectAnswer == my2ndAnswer + 1 or theCorrectAnswer == my2ndAnswer - 1:
            print('Close again, try once more!')
        elif theCorrectAnswer == my2ndAnswer:
            print('Good job!')
            break
        elif theCorrectAnswer != my2ndAnswer or theCorrectAnswer != my2ndAnswer + 1 or the2ndCorrectAnswer != my2ndAnswer - 1:
            print('You are to far off, my friend!')
            break
else:
	print('Wrong answer!')
print('Good bye ' + nameVar + '!')


#Super simple and insecure login
print('Please type in your username!')
print('Hint: its "emil"!')
usernameVariable1 = str(input())
while usernameVariable1 != 'emil':
    print('Wrong user! Please re-type your username!')
    usernameVariable1 = str(input())
    if usernameVariable1 == 'emil':
        break
print('Alrighty!')
print('Now, type in your password!')
print('Hint: it`s a quite common one..!')
userPassword1 = str(input())
while userPassword1 != '123':
    print('Wrong, dude..!')
    print('Try again!')
    userPassword1 = str(input())
    if userPassword1 == '123':
        break
print('You are now signed in, my friend!')


#Looking at the "for" variable. with the "in range" function.
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
