
#Loop: 
#repetition of an certain action again and again 
#Types of Loops :
# FOR LOOP AND WHILE LOOP
#FOR LOOP :
# It is used to repeat a ceratain actions over a sequence 
#it is used to iterate over a sequence 
#syntax:for var_name in sequence:

# list1= [1,2,3,4,5,6,7,8]
# for i in list1:
#     print(i)

# range(): It is used to generate numbers over a limit

# print(list(range(1,500)))

#len(): It is used to find the number of values in a sequence
# print(len(list1))
# str1='varsh'
# print(len(str1))
# names = ['kittu','nithin','varsh','sruthi']
# for name in range(len(names)):
#     print(name) 
# for name in names:
#     print(name)                   #direct access
# for i in range(len(names)):
#     print(names[i])               #accesing using indexing
# for i in range(len(names)):
#     print(names[i][0].upper())

# for i in names:
#     print(i[len(i) // 2])

#String concatenation and replication:
#adding two strings is called string concatenation.
# a='5'
# b='10'
# print(a+b)
# c='5'
# d=6
# print(c*d)  #replication: multipying a string with a number is called string replication

# name1 = 'Rahul'

# name2 = 'Keerthy'
# print(name1+ ' ' +name2)


for i in range(1,6):
    print('*'*i)
