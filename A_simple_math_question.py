#Emil B.B.
#Im doing some python excercises about flow control involving if, else, elif and while statements with some simple != & or operators.


#What is 2+2 my simple math question the sophisticated version.
theCorrectAnswer = 2 + 2
print('what is 2+2?')
myAnswer = int(input())
if theCorrectAnswer == myAnswer:
	print('Correct')
elif theCorrectAnswer == myAnswer + 1 or theCorrectAnswer == myAnswer - 1:
    print('You are close, try again!')
    while theCorrectAnswer == myAnswer + 1 or theCorrectAnswer == myAnswer - 1:
        my2ndAnswer = int(input())
        if theCorrectAnswer == my2ndAnswer + 1 or theCorrectAnswer == my2ndAnswer - 1:
            print('Try again, you are close')
        elif theCorrectAnswer == my2ndAnswer:
            print('Good job!')
            break
        elif theCorrectAnswer != my2ndAnswer or theCorrectAnswer != my2ndAnswer + 1 or the2ndCorrectAnswer != my2ndAnswer - 1:
            print('You are to far off, my friend')
            break
else:
	print('Wrong answer!')
print('Done!')
