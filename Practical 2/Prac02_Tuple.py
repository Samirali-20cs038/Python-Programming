#a. Write a Python program to create a tuple with different data types.
exa_tuple = ('Samir', 38, 152.33,True)
print(type(exa_tuple))
print()

#b. Write a Python program to create a tuple with numbers and print one item.
numbers = (1, 2, 3, 4, 5)
print(numbers[2])
print()

#c. Write a Python program to add an item in a tuple.
numbers = numbers + (6,)
print(numbers)
print()

#d. Write a Python program to convert a tuple to a string.
def  convertToString(tuple) :
    #intializing an empty string
    str = ''
    for item in tuple:
        str += item
    return str

tuple = ('S','A','M','I','R')
str = convertToString(tuple)
print(str)
print()

#e. Write a Python program to find the length of a tuple.
print(len(tuple))