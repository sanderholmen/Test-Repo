#Lists are an important part of programming. As the program grows, storing values in lists becomes more important.
#Lets take a look at the list function.
# listVariableOne = ['carrot', 'potato', 'lettuce'] #We are using square brackets to assign the values that are separated by commas in the list.
# listVariableOne #Calling the listVariableOne will print out the whole list including the squarebrackets -> ['carrot', 'potato', 'lettuce'].
# listVariableOne[1] #We are calling the listVariableOne and asking for the position 1 "index" (remember that it starts counting from 0). This means that 0 = carrot, 1 = potato and 2 = lettuce.

#We can also have lists containing lists.
#In this simple little program we select an item from two different lists.
#We have already set the variable for the list containing 3 countries and 3 cities.
#First we chose which list (country or city) then we chose item for example stockholm inside the city-list.


listVariableTwo = [['norway','sweden','denmark'],['oslo','stockholm','copenhagen']] #The syntax is basically [[','],[',']]
# listVariableTwo #This will output: [['norway', 'sweden', 'denmark'], ['oslo', 'stockholm', 'copenhagen']]
# listVariableTwo [0] #While this will output: ['norway', 'sweden', 'denmark']
# listVariableTwo [0][2] #And this will output: 'denmark'

print('We have to lists. One containing countries and another containing cities..!')
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
