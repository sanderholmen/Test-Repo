#Indexes for dictionaires can use many different datatypes, not just integers.
#The indexes for dictionaries ar ecalled "keys".
#A key with its associated value is called a "key value pair".

#Sintax for dictionary Datatype = variable = {'key': 'value', 'newkey': 'newvalue'...}
>>>dictionaryVar1 = {
'size':'large',
'colour': 'brown',
'length_cm': '15',
}
#We can access every value/item through its key argument.
>>> dictionaryVar1['size']
'large'
#Example use:
>>>print('The average length of a mans pinky is ' + str(int(dictionaryVar1['length_cm']) /2) + ' centimeters!')

#Unlike lists, all the items are unordered.
#A list:
>>>['cat','dog','pig'] == ['dog','pig','cat']
False
#A dictionary:
>>>{'1': 'cat', '2': 'dog', '3': 'pig'} == {'2': 'dog', '3': 'pig','1': 'cat'}
True

#Check if key is in dictionary:
>>>'width' in dictionaryVar1
False
for 'size' in dictionaryVar1:
    if 'size' == 'small':
        print('Nope!')
    elif 'size' == 'large':
        print('Yeah, dude!')
    else:
        print('What happened?')

#Listing keys, values and items from the dictionary under:
>>>dictionaryVar2 = {
'name':'emil',
'age': '30',
'sex': 'male',
}
#Listing the keys (the preset datatype in the dictionary) in dictionary using list():
>>>list(dictionaryVar2.keys())
['name', 'age', 'sex']
#Listing the values in the dictionary using list():
>>>list(dictionaryVar2.values())
['emil', '30', 'male']
>>>list(dictionaryVar2.items())
[('name', 'emil'), ('age', '30'), ('sex', 'male')]
