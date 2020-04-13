#It`s important to understand that datatypes matter when working with them interchangeably.

#Numbers and Characters
>>> int(10)
10
>>> str('hello')
'hello'
>>> int(str('10'))
10
>>> str(int(10))
'10'


#Tuples
>>> tuple('hello')
('h', 'e', 'l', 'l', 'o')
>>>tuple(('up', 'down', 10))
('up', 'down', 10)
#Convert a list to a tuple for mutability
>>>tuple(['up', 'down', 10])
('up', 'down', 10)


#Lists
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> list(['up', 'down', 10])
['up', 'down', 10]
#Convert a tuple to list for immutability
list(('up', 'down', 10))
['up', 'down', 10]


#Dictionary
>>>{'badpet': 'cat','goodpet': 'dog'}
{'badpet': 'cat', 'goodpet': 'dog'}
