#Lists are an important part of programming. As the program grows, storing values in lists becomes more important.
#Lets take a look at the list function.
# listVariableOne = ['carrot', 'potato', 'lettuce'] #We are using square brackets to assign the values that are separated by commas in the list.
# listVariableOne #Calling the listVariableOne will print out the whole list including the squarebrackets -> ['carrot', 'potato', 'lettuce'].
# listVariableOne[1] #We are calling the listVariableOne and asking for the position 1 "index" (remember that it starts counting from 0). This means that 0 = carrot, 1 = potato and 2 = lettuce.

#We can also have lists containing lists.
#In this simple little program we select an item from two different lists.
#We have already set the variable for the list containing 3 countries and 3 cities.
#First we chose which list (country or city) then we chose item for example stockholm inside the city-list.


# listVariableTwo = [['norway','sweden','denmark'],['oslo','stockholm','copenhagen']] #The syntax is basically [[','],[',']]
# # listVariableTwo #This will output: [['norway', 'sweden', 'denmark'], ['oslo', 'stockholm', 'copenhagen']]
# # listVariableTwo [0] #While this will output: ['norway', 'sweden', 'denmark']
# # listVariableTwo [0][2] #And this will output: 'denmark'
#
# print('We have two lists. One containing countries and another containing cities..!')
# print('Chose wether you want to select the country-list or the city-list')
# print('0 = ' + str(listVariableTwo [0])) #This prints out the first list inside the listVariableTwo.
# print('1 = ' + str(listVariableTwo [1])) #This prints out the second list inside the listVariableTwo.
# print('Type 0 or 1') #Lets ask user to type 0 or 1.
# userInput1 = int(input()) #We store the value in this variable.
#
# #First function is chosing which list to view.
# if userInput1 == 0: #If 0 was typed, we run this block.
#     print(listVariableTwo[0]) #We print out the first list of the two.
#     listVariableTwo = listVariableTwo[0] #Now we also set the variable to only hold the first list before we move on to the next function.
# elif userInput1 == 1:#If 1 was typed, we run this block.
#     print(listVariableTwo[1]) #We print out the second list of the two.
#     listVariableTwo = listVariableTwo[1] #Now we also set the variable to only hold the second list before we move on to the next function.
# else:
#     print('You did not type 0 or 1..') #If the user is imbecile and dont understand the instruction to type 0 or 1, well then.....
#
# #The next function is chosing one item/value inside the selected list.
# print('0 = ' + str(listVariableTwo [0])) #This prints out the first item in the previously selected list previous
# print('1 = ' + str(listVariableTwo [1])) #This prints out the second item in the previously selected list previous
# print('2 = ' + str(listVariableTwo [2])) #This prints out the third item in the previously selected list previous
#
# print('Type 0, 1 or 2 to select item')
# userInput2 = int(input())
# if userInput2 == 0: #If 0 was typed, we run this block.
#     print(listVariableTwo[0]) #We print out the first item in the list.
# elif userInput2 == 1: #If 1 was typed, we run this block.
#     print(listVariableTwo[1]) #We print out the second item in the list.
# elif userInput2 == 2: #If 2 was typed, we run this block.
#     print(listVariableTwo[2]) #We print out the third item in the list.
# else:
#     print('You did not type 0,1 or 2..') #If the user is imbecile and dont understand the instruction to type 0, 1 or 2; well then.....




#We can also refer to inddexes (items) in a list by using a negativ number, for example -> [-1].
#[-1] will refer to the last item.
#[-2] will refer to the second last.
#[-3] third last and so on..

#If we want to select multiple items (slices) we can do as such:
#If we assigned listVariableTwo = ['norway','sweden','denmark']
#listVariableTwo [0:2] will print out ['norway', 'sweden'] since we start from 0 and print out position 0 - 1 = length of list items 2.
#We can also do listVariableTwo [1:3] and it will print out ['sweden', 'denmark'].

################################################################################
#Qoute Al_Sweigart: Automate the Boring stuff with Python.
# As a shortcut, you can leave out one or both of the indexes on either side
# of the colon in the slice. Leaving out the first index is the same as using 0 ,
# or the beginning of the list. Leaving out the second index is the same as
# using the length of the list, which will slice to the end of the list. Enter the
# following into the interactive shell:
    # >>> spam = ['cat', 'bat', 'rat', 'elephant']
    # >>> spam[0:4]
    # ['cat', 'bat', 'rat', 'elephant']
    # >>> spam[1:3]
    # ['bat', 'rat']
    # >>> spam[0:-1]
    # ['cat', 'bat', 'rat']
    #>>> spam[:]
    #['cat', 'bat', 'rat', 'elephant']
################################################################################

# #Update the list through user input can also be done.
# #Lets look at changing an index (item) inside a list.
# listVariableThree = ['first_record','second_record','third_record']
# print('We have ' + str(listVariableThree) + ' in this list!')
# print('Write down the name of the item that you want stored in the first_record!')
# listVariableThree[0] = str(input()) #Using input() function and set listVariableThree[0] changes the first_record (notice the [0] after the variable).
#
# print('Thanks, I have now stored ' + str(listVariableThree[0]) + 'in your first_record')
# print('Your list now contains ' + str(listVariableThree))
# print('Now tell me what the other two items would be in the second_record and third_record')
# print('Type the first item and then press enter, then the second item followed by another enter!')
# listVariableThree[1:3] = str(input()) + str(input()) #We change two indexes by using two input() function separated with a "+". Also notice the [1:3] (starts at 1 which is the second record and counts up to but not including 3).
# print('Your list now contains ' + str(listVariableThree) + '. Thanks for stopping by!')


# #Lets see how we can find the length of a list.
# #The len() function counts letter, indexes etc and can be used in this case.
# listVariableFour = ['monitor','speakers','display','keyboard','mouse','microphone','gamepad']
# print(len(listVariableFour)) #We put the len() function inside a print() function so that it prints out the length of the list -> in this case the total amount of values (indexes).



#Combining lists is also possible.
# #The + operator can combine lists the same way it combines strings (string concatenation).
# listVariableFive = ['one','two','three']
# listVariableSix = [1,2,3]
# print((listVariableFive)+(listVariableSix)) #This prints out both lists.
# #Lets count the length of both..
# print(len((listVariableFive)+(listVariableSix))) #We count all the items listet.



#Almost forgot... we should also be able to delete records!
#For deleting we use the del statement.
#I`ll also add some other functions that I`ve learned so far (try and while loop) to make this more sophisticated.
# listVariableSeven = ['emil','jan','thomas'] #We prelist 3 indexes (items).
# print('Type 1, 2 ,3 or 4 and then press enter to delete a name!')
# print('1 = ' + listVariableSeven[0])
# print('2 = ' + listVariableSeven[1])
# print('3 = ' + listVariableSeven[2])
# print('4 = cancel') #We add a cancel option so that the user can cancel out and not be forced to delete a record.
# delListSeven = 4 #We just set the variable that we will input to a value that will trigger the while loop.
# while delListSeven != 4 or delListSeven != 3 or delListSeven != 2 or delListSeven != 1: #Since our variable is not 1, 2, 3 or 4 (since it is preset to 5) the while loop triggers.
#     try: #try statement lets the program try. This means essentially that if user input throws an error which in this case if we type characters since we spesifically ask for integer (notice the int(input()) we can set an action for that specific error.
#         delListSeven = int(input()) #Remember that we need an int before the input() statement so that the if function works when equal input number.
#         if delListSeven == 1 or delListSeven == 2 or delListSeven == 3 or delListSeven == 4: #We break out only if the value we type in is 1, 2, 3 or 4.
#             break
#         else:
#             print('Wrong number selection!')
#             print('Try again..!')
#             print('Select 1, 2, 3 or 4 then hit enter..')
#             continue
#     except ValueError: #This is the error exception. We run the lines under if the line under the "try" statement will give us the ValueError which it will if we type in characters.
#         print('Dont type characters!')
#         print('Try again..!')
#         print('Select 1, 2, 3 or 4 then hit enter..')
#         continue #We jump back to the "try" statement using this continue statement.
# #The lines under are ran depending on which input made it through the while loop.
# if delListSeven == 1:
#     del listVariableSeven[0]
# elif delListSeven == 2:
#     del listVariableSeven[1]
# elif delListSeven == 3:
#     del listVariableSeven[2]
# else:
#     print('Your list was unchanged..!')
# print('Your list now looks like this ' + '"' + str(listVariableSeven) + '".')





#list() function returns a list form of values you pass to it.
#An example...
#list('Hello') #This will list every letter in its own index and print it out like this:
#list('Hello')
#['H', 'e', 'l', 'l', 'o']

#Write records to list.
# #Giving the list a name and putting multiple values into the list:
# myEmployees = [] #This is an empty list called myEmployees.
# while True:
#     print('Name of employee ' + str(len(myEmployees) +1) + ' (enter nothing to stop!):')
#     employeeName = input()
#     if employeeName == '':
#         break
#     myEmployees = myEmployees + [employeeName] #We concatenate the list.
# print('The employees names are:')
# for employeeName in myEmployees: #The line under will run for any item/value/index in the list myEmployees.
#     print(' ' + employeeName)
# while True: #We dont really need this while loop, but in this case it does not seem to introduce any errors or bugs, so why not for learning sake..
#     if 'emil' in myEmployees: #Runs line under if emil is in the list.
#         print('Yes, emil is listed here!')
#         break
#     elif 'emil' not in myEmployees: #Runs line under if emil is not listed.
#         print('emil is not listed here!')
#         break
# print('Done')


# #We can also use the list() function to list all numbers in the range() function.
# #Say for example that we have range (0,10,2) 0 - 10 and 2 increments.
# list(range(-10,12,3)) #This will print out numbers from -10 to 11 (not counting 12) with an increment of 3. -> [-10, -7, -4, -1, 2, 5, 8, 11]
# #Lets put it in a variable..
# listVariableEight = list(range(-10,12,3))
# print(listVariableEight)

#
# #Lets organize the stuff in a list using the for in range function.
# listVariableNine = ['phone','laptop','wallet','glasses'] #A list of my stuff..
# for rangeVariable1 in range(len(listVariableNine)): #Notice that we put a len() function inside the for in range() statement. This will print out the number/order of all items in list.
#     print('Item ' + str(rangeVariable1) + ' in my list off stuff is: ' + listVariableNine[rangeVariable1]) #Notice that since we concatenate a string in the print statement, we have to put str(rangeVariable1) because the in range variable contains only integers.




# #We can do a "database" like scheme for our list by giving a name-variable to each index.
# carVariable = ['audi','yellow','2004'] #First we assign the list to a a variable..
# brand, colour, year = carVariable #Then we give names to the items in relation to where they are stored; audi is in index 0 so we put brand first, then yellow which corresponds to the 2nd value = index 1 and so forth..  )
# #We can also do this in one line..
# brand, colour, year = 'honda','red','2009'
# #To see if something is in the list we can use in or not in.
# 'honda' in carVariable #If honda is found in any of the indexes it will return "True", if not; it will return "False".
# #Multiply values in list:
# carVariable *= 3


# List Methods...
# #Find the index position and or return a ValueError with the index() method.
# #Syntax = thelistvariable.index('indexname')
# foodVariable = ['pizza','taco','salomon','chicken','spaghetti']
# foodVariable.index('pizza') #This will return 0 becuase pizza is the first index.
# foodVariable.index('pancake') #This will return:
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # ValueError: 'pancake' is not in list
#
# #Adding (appending) an item to the list and/or inserting an item. Syntax = variable.append('item').
# foodVariable.append('pancake') #This will add 'pancale' as in the last index.
# foodVariable.index('pancake') #This will now return the number for the last item in the list which is 5.
# foodVariable.insert(2,'lamb') #This will add 'lamb' in the third [2] 0,1,2 record and bump the rest of the items up 1 step.
# #Removing with the remove() list methond. Syntax = variable.remove('item').
# #Just like using "del variable[0]"" for deleting index item 0, we can use the remove() function.
# foodVariable.remove('pizza') #This will delete the record by typing in the name instead of index number. Keep in mind that if you have pizza stored twice or more, it will only remove the first item in the list.

#For a list of numbers we can use the sort() method to sort them.
listVariableTen = [15,-35,75,47,12,-12,-63,-1,-2,73,12,-35]
listVariableTen.sort() #If we do a print(listVariableTen) we will see that this list is sorted from lowest to highest number.
#This also works for alphabetical order.
listVariableEleven = ['plane','boat','car','train','submarine']
listVariableEleven.sort() #When printing out the list it will output -> ['boat', 'car', 'plane', 'submarine', 'train']
listVariableEleven.sort(reverse=True) #This sorts it the opposite way. -> ['train', 'submarine', 'plane', 'car', 'boat']
