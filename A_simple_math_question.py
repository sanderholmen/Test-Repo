# Emil B.B.
# Im doing some python excercises about flow control involving if, else, elif and while statements with some simple != & or operators.
# A good example of flow control usage can be a math question that will give multiple outputs depending on the users input.

# What is 2+2 my simple math question the sophisticated version.
print('Hello, can you type you`r name in for me please?!')
nameVar = ('')
while nameVar != bool(0):
	nameVar = str(input())
	break
print('Good to meet you, ' + nameVar + '!')

theCorrectAnswer = 2 + 2
print('what is 2+2?')
myAnswer = int(input())
if theCorrectAnswer == myAnswer:
	print('Correct! You are a very smart person!')
elif theCorrectAnswer == myAnswer + 1 or theCorrectAnswer == myAnswer - 1:
    print('You are close, try again!')
    while theCorrectAnswer == myAnswer + 1 or theCorrectAnswer == myAnswer - 1:
        my2ndAnswer = int(input())
        if theCorrectAnswer == my2ndAnswer + 1 or theCorrectAnswer == my2ndAnswer - 1:
            print('Close again, try once more!')
        elif theCorrectAnswer == my2ndAnswer:
            print('Good job!')
            break
        elif theCorrectAnswer != my2ndAnswer or theCorrectAnswer != my2ndAnswer + 1 or \
		the2ndCorrectAnswer != my2ndAnswer - 1:
            print('You are to far off, ' + nameVar + '.. Good bye, my friend!')
            break
else:
	print('Wrong answer, stupid!')
print('Good bye ' + nameVar + '!')
