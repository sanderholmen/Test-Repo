string = 'What`s up, my name is Emil and I`m learning Python!'
dictionary = {}

for characters in string.upper():
    dictionary.setdefault(characters, 0)
    dictionary[characters] = dictionary[characters] + 1

print(dictionary)
