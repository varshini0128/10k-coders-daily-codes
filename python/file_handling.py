'''
Docstring for file_handling
functions:
        1)read
        2)write
        3)open
        4)close
        5)seek
        6)tell
modes:
        1)x  ==> create new file , write
        2)w  ==> create file , write
        3)r  ==> read only
        4)a  ==> append 
        5)r+
        6)w+
        7)a+
        8)rb
        9)wb
'''

# k=open('abc.py','x')
# k.write('python')

# p=open('ab.py','x')
# p.write('python')

# k=open('abc.txt','w')
# k.write('items=300')

# h=open('abc.txt','r')
# print(h.read())
# h.close()

#we can also create a new file using append 'a' mode 

# l=open('abc.py','a') 
# l.write('python daily codes and file handing concept')
# l.close()
 
# s=open('abc.py','a')
# s.write('\n #this is an example file created to practise file handling concepts')
# s.close()

# with open('demo1.txt','w') as k:
#     k.write('This is w mode')

# no need of closing when we use with keyword to createor write

# r ==> read only w ==> only write  a ==> only append
# w+ ==> write, read
# r+ ==> read, write
# a+ ==> append, read


# # w+ ==> create, write, read
# with open('class2.txt' , 'w+') as k:
#     k.write('This is w+ mode ==> write and read')
#     k.seek(0)
#     data = k.read()
#     print(data)
#     print(k.tell())    #gives the current position of cursor

# m=open('class2.txt','w+')
# m.write('hello w+ mode')







# # r+ ==>read, write
# j=open('class2.txt',)



# k=open('coffee.png','rb')
# data=k.read()
# new=open('copy.png','wb')
# new.write(data)


# file lo no of lines count no of word no of characters 
# k=open('demo1.py','r')
# c=0
# if k.tell()=='#':
#     c+=1
# print(c)
# print('no of lines in demo1.py file is ', c)

k=open('demo1.py','r')
lines=k.readlines()
print(lines)
no_of_lines=len(lines)
print(no_of_lines)


# no_of_words=0
# for line in lines:
#    s= len(line.split())
#    no_of_words+=s
# print(no_of_words)


# no_of_char=0
# for line in lines:
#    s1= len(line)
#    no_of_char+=s1
# print(no_of_words)

vowel_count=0
for i in lines:
   for j in i:
      if j in "aeiouAEIOU":
        vowel_count+=1
print(vowel_count)


import os
if os.path.exists('ab.py'):
   os.remove('ab.py')

