'''
Comprehensions: 
Comprehensions are used to generate sequences from an existing sequence in simple and efficient way.
Types of comprehensions:
list comprehension
set comprehension
dictionary comprehension
tuple comprehension
'''
list1=[1,2,3,4,5]
# list2=[]
# for i in list1:
#     s=i**2
#     list2+=[s]
# print(list2)

# list3=[i*i for i in list1]      # list comprehension
# print(list3)

'''
List comprehension:
syntax: [expression ]
'''
list4=list(range(1,11))
evenlist=[i for i in list4 if i%2==0]
print(evenlist)

names=['kiran','uday','kavya','why','try','myth']
list2=[]
vowels='aeiouAEIOU'
for i in names :
    for char in i:
        if char in vowels  :
            break
    else:
        list2+=[i]
print(list2)

#list of domains from a string 
list5=['user1@gmail.com','user2@yahoo.com','user3@microsoft.com']
domains=[email.split('@')[1] for email in list5]
print(domains)