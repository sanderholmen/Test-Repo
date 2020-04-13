#Let`s take a look at variables.

#Syntax for string:
myVariableName = 'the string I want'
#Syntax for integer:
myVariableName = 10

#We can have mulitple variables pointing to the same value.
honda = 'my current car'
opel = honda #This make opel point to honda which points to the string 'my current car' and typing in opel will print out excactly that.

#We can clear (delete value) in a variable with None.
honda = None #This will clear the honda variable leaving only opel with the "my current car" value.

#We can do multiple changes in one line:
#First we add 3 variables in on line:
myVariable1, myVariable2, myVariable3 = 'abc', 'def', 'ghi'
#Then we swap all 3 in on line:
myVariable1, myVariable2, myVariable3 = myVariable2, myVariable3, myVariable1

#In programming you`ll often come across "variable + 1" for increments and other stuff using augmented assignment operators.
myVariable = 1 #We`ll just assign a variable first so that we can take a look at what this is all about.
#This is what it looks like when we are not using the augmented assignment operators:
myVariable = myVariable + 1
#This is what it looks like when we are using the augmented assignment operators:
myVariable += 1 #We essentially just skipped typing myVariable the second time and swapped the = and +.
#We can do this with +, - *, / and %.
myVariable -= 2
myVariable *= 2
myVariable /= 2
myVariable %= 2

#We can do string and list replication with the * operator.
myVariable = ' you'
myVariable *= 3
>>>print('Where are' + str(myVariable) + '!!!')
