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
