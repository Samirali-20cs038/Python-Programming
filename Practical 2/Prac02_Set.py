#a. Write a Python program to add member(s) in a set and clear a set
animal = {'Cat', 'Dog', 'Horse'}
print(animal)
animal.add('Elephant')
print(animal)
animal.clear()
print(animal)
print()

#b. Write a Python program to remove an item from a set if it is present in the set.
phone = {'samsung' , 'iphone' , 'realme', 'nokia'}
print(phone)
phone.remove('realme')
print(phone)
print()

#c. Write a Python program to create an intersection, Union, difference of sets.
fruits = {'Apple','Banana','Lemon'}
#print(fruits)
vegetables = {'Potato','Lemon','Onion'}
#print(vegetables)
print(fruits.union(vegetables))
print(fruits.intersection(vegetables))
print()

#d. Write a Python program to find maximum and the minimum value in a set.
set = { 7 ,63 , 786 , 128}
print(max(set))
print(min(set))
print()

#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
##for list:
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))
print()

#for tuple
def countX(tup, x):
    count = 0
    for ele in tup:
        if (ele == x):
            count = count + 1
    return count

tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8
print(countX(tup, enq))
print(countX(tup, enq1))
print(countX(tup, enq2))