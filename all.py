#This "all.py" file contains most of what I`ve written in python while Im in my learning phase..


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


#Error handeling and how to work with it.
#Handeling errors and examples of treating a function as a "black box" when all you want is the output of a function.
def randomVariable5(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('No, dont divide by zero my friend!')
#Since dividing by zero prints an error message, notice the first print statement (0); the program will output an error saying ZeroDivisionError: division by zero.
#To overcome this so that the program can continue, you can add in "try and "except"" statements.
print(randomVariable5(0))
print(randomVariable5(1))
print(randomVariable5(2))
print(int(randomVariable5(3)))
print(float(randomVariable5(5)))
print(int(randomVariable5(21)))


#Another example..
#This program lets you chose a number, but what if you type a string of characters instead?
print('Type a number, please!')
randomVariable6 = input()
if int(randomVariable6) > 5:
    print('Thats a high number!')
else:
    print('Thats a low number!')

#If you type anything other than integers (number) it will crash with the error message "ValueError: invalid literal for int() with base 10: 'as'".
#This program fixes this by using the try and except statements.
#This is a good example of the use of an input validation.
print('Type a number, please!')
randomVariable7 = input()

try:
    if int(randomVariable7) > 5:
        print('Thats a high number!')
    else:
        print('Thats a low number!')
except ValueError: #You can see that we put the first line in the error output in the except statement making the program run the lines under if this error appears.
    print('You did not type in a number!')



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



#Learning the list function..
#Lists can hold multiple values. It ca neveb hold lists inside of a list.
listVariableTwo = [['norway','sweden','denmark'],['oslo','stockholm','copenhagen']] #The syntax is basically [[','],[',']]
# listVariableTwo #This will output: [['norway', 'sweden', 'denmark'], ['oslo', 'stockholm', 'copenhagen']]
# listVariableTwo [0] #While this will output: ['norway', 'sweden', 'denmark']
# listVariableTwo [0][2] #And this will output: 'denmark'

print('We have two lists. One containing countries and another containing cities..!')
print('Chose wether you want to select the country-list or the city-list')
print('0 = ' + str(listVariableTwo [0])) #This prints out the first list inside the listVariableTwo.
print('1 = ' + str(listVariableTwo [1])) #This prints out the second list inside the listVariableTwo.
print('Type 0 or 1') #Lets ask user to type 0 or 1.
userInput1 = int(input()) #We store the value in this variable.

#First function is chosing which list to view.
if userInput1 == 0: #If 0 was typed, we run this block.
    print(listVariableTwo[0]) #We print out the first list of the two.
    listVariableTwo = listVariableTwo[0] #Now we also set the variable to only hold the first list before we move on to the next function.
elif userInput1 == 1:#If 1 was typed, we run this block.
    print(listVariableTwo[1]) #We print out the second list of the two.
    listVariableTwo = listVariableTwo[1] #Now we also set the variable to only hold the second list before we move on to the next function.
else:
    print('You did not type 0 or 1..') #If the user is imbecile and dont understand the instruction to type 0 or 1, well then.....

#The next function is chosing one item/value inside the selected list.
print('0 = ' + str(listVariableTwo [0])) #This prints out the first item in the previously selected list previous
print('1 = ' + str(listVariableTwo [1])) #This prints out the second item in the previously selected list previous
print('2 = ' + str(listVariableTwo [2])) #This prints out the third item in the previously selected list previous

print('Type 0, 1 or 2 to select item')
userInput2 = int(input())
if userInput2 == 0: #If 0 was typed, we run this block.
    print(listVariableTwo[0]) #We print out the first item in the list.
elif userInput2 == 1: #If 1 was typed, we run this block.
    print(listVariableTwo[1]) #We print out the second item in the list.
elif userInput2 == 2: #If 2 was typed, we run this block.
    print(listVariableTwo[2]) #We print out the third item in the list.
else:
    print('You did not type 0,1 or 2..') #If the user is imbecile and dont understand the instruction to type 0, 1 or 2; well then.....




#Update the list through user input can also be done.
#Lets look at changing an index (item) inside a list.
listVariableThree = ['first_record','second_record','third_record']
print('We have ' + str(listVariableThree) + ' in this list!')
print('Write down the name of the item that you want stored in the first_record!')
listVariableThree[0] = str(input())

print('Thanks, I have now stored ' + str(listVariableThree[0]) + 'in your first_record')
print('Your list now contains ' + str(listVariableThree))
print('Now tell me what the other two items would be in the second_record and third_record')
print('Type the first item and then press enter, then the second item followed by another enter!')
listVariableThree[1:3] = str(input()) + str(input())
print('Your list now contains ' + str(listVariableThree) + '. Thanks for stopping by!')





#Lets see how we can find the length of a list.
#The len() function counts letter, indexes etc and can be used in this case.
listVariableFour = ['monitor','speakers','display','keyboard','mouse','microphone','gamepad']
print(len(listVariableFour)) #We put the len() function inside a print() function so that it prints out the length of the list -> in this case the total amount of values (indexes).





#Almost forgot... we should also be able to delete records!
#For deleting we use the del statement.
#I`ll also add some other functions that I`ve learned so far (try and while loop) to make this more sophisticated.
listVariableSeven = ['emil','jan','thomas'] #We prelist 3 indexes (items).
print('Type 1, 2 ,3 or 4 and then press enter to delete a name!')
print('1 = ' + listVariableSeven[0])
print('2 = ' + listVariableSeven[1])
print('3 = ' + listVariableSeven[2])
print('4 = cancel') #We add a cancel option so that the user can cancel out and not be forced to delete a record.
delListSeven = 4 #We just set the variable that we will input to a value that will trigger the while loop.
while delListSeven != 4 or delListSeven != 3 or delListSeven != 2 or delListSeven != 1: #Since our variable is not 1, 2, 3 or 4 (since it is preset to 5) the while loop triggers.
    try: #try statement lets the program try. This means essentially that if user input throws an error which in this case if we type characters since we spesifically ask for integer (notice the int(input()) we can set an action for that specific error.
        delListSeven = int(input()) #Remember that we need an int before the input() statement so that the if function works when equal input number.
        if delListSeven == 1 or delListSeven == 2 or delListSeven == 3 or delListSeven == 4: #We break out only if the value we type in is 1, 2, 3 or 4.
            break
        else:
            print('Wrong number selection!')
            print('Try again..!')
            print('Select 1, 2, 3 or 4 then hit enter..')
            continue
    except ValueError: #This is the error exception. We run the lines under if the line under the "try" statement will give us the ValueError which it will if we type in characters.
        print('Dont type characters!')
        print('Try again..!')
        print('Select 1, 2, 3 or 4 then hit enter..')
        continue #We jump back to the "try" statement using this continue statement.
#The lines under are ran depending on which input made it through the while loop.
if delListSeven == 1:
    del listVariableSeven[0]
elif delListSeven == 2:
    del listVariableSeven[1]
elif delListSeven == 3:
    del listVariableSeven[2]
else:
    print('Your list was unchanged..!')
print('Your list now looks like this ' + '"' + str(listVariableSeven) + '".')



#Write records to list.
#Giving the list a name and putting multiple values into the list:
myEmployees = [] #This is an empty list called myEmployees.
while True:
    print('Name of employee ' + str(len(myEmployees) +1) + ' (enter nothing to stop!):')
    employeeName = input()
    if employeeName == '':
        break
    myEmployees = myEmployees + [employeeName] #We concatenate the list.
print('The employees names are:')
for employeeName in myEmployees: #The line under will run for any item/value/index in the list myEmployees.
    print(' ' + employeeName)
while True: #We dont really need this while loop, but in this case it does not seem to introduce any errors or bugs, so why not for learning sake..
    if 'emil' in myEmployees: #Runs line under if emil is in the list.
        print('Yes, emil is listed here!')
        break
    elif 'emil' not in myEmployees: #Runs line under if emil is not listed.
        print('emil is not listed here!')
        break
print('Done!')


#We can also use the list() function to list all numbers in the range() function.
#Say for example that we have range (0,10,2) 0 - 10 and 2 increments.
list(range(-10,12,3)) #This will print out numbers from -10 to 11 (not counting 12) with an increment of 3. -> [-10, -7, -4, -1, 2, 5, 8, 11]
#Lets put it in a variable..
listVariableEight = list(range(-10,12,3))
print(listVariableEight)


#Lets organize the stuff in a list using the for in range function.
listVariableNine = ['phone','laptop','wallet','glasses'] #A list of my stuff..
for rangeVariable1 in range(len(listVariableNine)): #Notice that we put a len() function inside the for in range() statement. This will print out the number/order of all items in list.
    print('Item ' + str(rangeVariable1) + ' in my list off stuff is: ' + listVariableNine[rangeVariable1]) #Notice that since we concatenate a string in the print statement, we have to put str(rangeVariable1) because the in range variable contains only integers.


#We can do a "database" like scheme for our list by giving a name-variable to each index.
carVariable = ['audi','yellow','2004'] #First we assign the list to a a variable..
brand, colour, year = carVariable #Then we give names to the items in relation to where they are stored; audi is in index 0 so we put brand first, then yellow which corresponds to the 2nd value = index 1 and so forth..  )
#We can also do this in one line..
brand, colour, year = 'honda','red','2009'
#To see if something is in the list we can use in or not in.
'honda' in carVariable #If honda is found in any of the indexes it will return "True", if not; it will return "False".

# List Methods...
#Find the index position and or return a ValueError with the index() method.
#Syntax = thelistvariable.index('indexname')
foodVariable = ['pizza','taco','salomon','chicken','spaghetti']
foodVariable.index('pizza') #This will return 0 becuase pizza is the first index.
foodVariable.index('pancake') #This will return:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 'pancake' is not in list

#Adding (appending) an item to the list and/or inserting an item. Syntax = variable.append('item').
foodVariable.append('pancake') #This will add 'pancale' as in the last index.
foodVariable.index('pancake') #This will now return the number for the last item in the list which is 5.
foodVariable.insert(2,'lamb') #This will add 'lamb' in the third [2] 0,1,2 record and bump the rest of the items up 1 step.
#Removing with the remove() list methond. Syntax = variable.remove('item').
#Just like using "del variable[0]"" for deleting index item 0, we can use the remove() function.
foodVariable.remove('pizza') #This will delete the record by typing in the name instead of index number. Keep in mind that if you have pizza stored twice or more, it will only remove the first item in the list.


#For a list of numbers we can use the sort() method to sort them.
listVariableTen = [15,-35,75,47,12,-12,-63,-1,-2,73,12,-35]
listVariableTen.sort() #If we do a print(listVariableTen) we will see that this list is sorted from lowest to highest number.
#This also works for alphabetical order (or ASCII-betical order since upper case characters will come before lower case characters).
listVariableEleven = ['plane','boat','car','train','submarine']
listVariableEleven.sort() #When printing out the list it will output -> ['boat', 'car', 'plane', 'submarine', 'train']
listVariableEleven.sort(reverse=True) #This sorts it the opposite way. -> ['train', 'submarine', 'plane', 'car', 'boat']
#Remember that lists with numbers and characters can`t be sorted. It will throw out an unordable types error.
#Taking a look at the upper and lower characters in the list.
listVariableEleven = ['Plane','boat','Car','Train','submarine','motorbike','thanks','Spaceshuttle'] #It will output -> ['Car', 'Plane', 'Spaceshuttle', 'Train', 'boat', 'motorbike', 'submarine', 'thanks']
#For true alphabetical order we have to convert the upper case characters to lowercase.
listVariableEleven.sort(key=str.lower) #Now we have -> ['boat', 'Car', 'motorbike', 'Plane', 'Spaceshuttle', 'submarine', 'thanks', 'Train']


#Get a random value from the list. A magic 8 ball program.
import random #We need to import the random module.
#We store the list in randomVariable9.
randomVariable8 = [
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
]
randomVariable9 = int(randomVariable8[random.randint(0,len(randomVariable8)-1)]) #We store one random item from the list in randomVariable9.
if randomVariable9 == int(1):
    print('Today I`m having ' + str(int(randomVariable9)) + ' slice of pizza for dinner')
else:
    print('Today I`m having ' + str(int(randomVariable9)) + ' slices of pizza for dinner')


#A list and a string is basically the same if you consider the fact that every letter in a string has its own index. We can see this by passing a string inside a list() function.
list('Hello!') #This will print out: ['H', 'e', 'l', 'l', 'o', '!'] in a python shell.
#What can be done with lists can often also be done with strings.
listVariableTen = 'Hello!'
listVariableTen[0] #This will print out: 'H' (the first character in the variable).
listVariableTen[1:4] #This will print out: 'ell' ([1:4] means index 1 to 4 not counting 4 or the first one since it starts counting from 0).
listVariableTen[-2] #This will print out: 'o' ([-2] means counting backwards 2 steps from the last index).
#The one difference is that a string cannot be changed. They are immutable..
listVariableTen[3] = 'p' #This will throw out a TypeError: 'str' object does not support item assignment
#The right way to modify a string is to create a new string by using 'slices' then store it as a new variable. -> a slice looks like this: variablename[0:10].
listVariableEleven = 'Emil is a nerd!'
modifiedlistVariableEleven = listVariableEleven[0:10] + 'proffessional' + listVariableEleven[9:15] #listVariableEleven[0:10] = "Emil is a " listVariableEleven[9:15] = " nerd!". [0:10] is a slice..



#Taking a look at the copy.deepcopy() function.
#Until now we`ve been looking at ways to reference lists and not really copying them to have a complete seperate list.
#We can import the copy module to do this.
import copy #Import the copy module so that we can run the copy.deepcopy() function.
listVariableTwelve = [
'rice',
'ham',
'tomato',
'potato',
'spaghetti',
'steak',
'cod',
'lettuce'
]
copiedlistVariableTwelve = copy.deepcopy(listVariableTwelve) #Do a copy of the listVariableTwelve and reference the copy to the new variable copiedlistVariableTwelve.

copiedlistVariableTwelve.append('cucumber') #Now we modify the copiedlistVariableTwelve to store one more value.
listVariableTwelve[3] = ('apple') #Lets also modify the first list swapping out potato with apple.

print(listVariableTwelve) #Will print out: ['rice', 'ham', 'tomato', 'potato', 'spaghetti', 'steak', 'cod', 'lettuce']
print(copiedlistVariableTwelve)#Will print out: ['rice', 'ham', 'tomato', 'potato', 'spaghetti', 'steak', 'cod', 'lettuce', 'cucumber']
