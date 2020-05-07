# This is only for learning sake.
# In modern days, login solutions will never
# include any clear text handeling of passwords.
# Databases usually stores a hash value that
# can only be calculated one way,
# and that is from the users input (password).
# Anyway, to understand the concept;
# this is a fairly simple login script.
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
