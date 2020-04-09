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
