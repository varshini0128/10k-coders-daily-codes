#Enumerate and Zip functions:
# Enumerate: It is used to give index to a sequential data 
# If you dont pass a specific index value to start with,it starts from zero
#Real world usage: 
list1=[]
enumerate(list1)    # We cannot access a enumerated data directly inorder to access it we need to convert it into a sequence 

fruits=['mango','banana','guava','orange','apple','dragon fruit']
for ind,fruit in enumerate(fruits,start=10):
    print(ind,fruit)
    if fruit == 'apple':
        print('index of ',fruit,'is',ind)
    elif fruit == 'banana':
        print(f'index of {fruit} is {ind}')

print(enumerate(fruits))
#When we try to convert a enumerated data into a sequence it returns a sequence of pairs of tuples of index and the value
print(list(enumerate(fruits)))
print(dict(enumerate(fruits)))


# Task :
# Write a program to provide a sequence of names of students as a list and cconvert the list into dictionary with index values

student_list=['Varshini','Ram','Ravi','Sita','Geetha']
print(dict(enumerate(student_list)))
dict1={'name':'varsh','age':'22','place':'hyd'}
# for ind,i in enumerate(dict1):
print(dict(enumerate(dict1.items())))



#Zip(): It i used to combine more than one sequence into a sequence of tuples, the tuple consist of one value from each sequence
names=['varsh','ram','ravi','sita']
marks=[77,88,99,66,]
dept=['ece','iot','cse','aiml']
print(list(zip(names,marks,dept)))    #If you pass the sequences with uneven number of values to azip function then it generates tuples upto the sequence with least number of values
# print(dict(zip(names,marks,dept))) # error
print(dict(zip(names,(zip(marks,dept) ))))



for name,mark,dep in zip(names,marks,dept):
    print(f"{name} has scored {mark} marks in {dep}")
    # print(name,'has scored',mark, 'marks in',dep)

names=['varsh','ram','ravi','sita']
marks=[77,88,99,66,]
dept=['ece','iot','cse','aiml']
# {'varsh': (77, 'ece'), 'ram': (88, 'iot'), 'ravi': (99, 'cse'), 'sita': (66, 'aiml')}
# print(dict(marks,dept))


result = {}

result = {names[i]: (marks[i], dept[i]) for i in range(4)}
print(result)

