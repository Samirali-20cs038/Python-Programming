def Merge(Student,Teacher) :
    return (Teacher.update(Student))
Student = {
    'S_name': 'SamirAli',
    'S_id': '20CS038',
    'Age': 18
}
print(Student)

#a. Write a Python script to check whether a given key already exists in a dictionary.
print('S_name' in Student)
print('S_id' in Student)
print('Age' in Student)
print()

#b. Write a Python script to merge two Python dictionaries.
Teacher = {
    'T_name': 'Trusha Patel',
    'Subject': 'Python'
}
Merge(Student, Teacher)
print(Teacher)
print()

#c. Write a Python program to sum all the items in a dictionary.
Marks = {
     'sub1': 80,
     'sub2': 75,
     'sub3': 67
}
print(sum(Marks.values()))
print()

#d. Write a Python script to add a key to a dictionary.
Sample_dict = {0: 10, 1: 20}
Sample_dict[2] = 30
print(Sample_dict)
print()

#e. Write a Python script to concatenate following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for c in (dic1, dic2, dic3) : dic4.update(c)
print(dic4)