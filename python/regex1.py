import regex as re 

# functions
'findall'
d='built-in module named to work with regular expressions'

res= re.findall("module",d)
print(res)

# 'match'->it checks first str with frst string of the given string
res=re.match('ajay','ajay kumar')
print(res)


'fullmatch'
res=re.fullmatch('ajay kumar','ajay kumar')
print(res)

'search'
d='built-in module named to work with regular expressions'
res=re.search('module',d)
print(res)


'sub'
s='python@program#hello$'
res=re.sub('[^A-Za-z0-9]',' ',s)
print(res,"88888888888888")


# \d - any digit from 0 to 9
# \D - any non digit character
# \s - any white space character
# \S - any non white space character
# \w - any alphanumeric character(a-z,A-Z,0-9)
# \W - any non alphanumeric character



# common regex symbols/metacharacters
# . - any character except new line
# * - 0 or more than 0 times
# + - 1 or more than one time
# $ - end of the string
# ? - 0 or 1 time only
# {m} - m times
# {m,n} - m to n times
# [a,b,c] - either a or b or c
# [a-z] - any lowercase letter


mobile=int(input('Enter mobile number:'))
res=re.fullmatch('[6-9][0-9]{9}',str(mobile))
if res:
    print('valid mobile number')
else:
    print('invalid mobile number')

s=' my mobile number is 7842259549'

res=re.findall('\d+',s)
print(res)


s=' my 789 mobile 456 number is 7842259549'

res=re.findall('\d+',s)
print(res)

s='my 789 mobile & $ @ 456 number is 7842259549'

res=re.findall('\D',s)
print(res,'00000000000000000000000000000000000000000000')


# 7845129632




26/2/2026

import regex

h=['ravi@gmail.com','sai@gmail.com','sita@gmail.com','raju@gmail.com']
for x in h:
    res=regex.fullmatch(r'[a-z]+@gmail\.com',x)
    if res!=None:
        print(x)


s='''lorem ipsum dolor sit amet,ravi@gmail.com consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis@gmail.com nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute sai@gmail.com irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt@gmail.com in culpa qui officia deserunt mollit
anim@gmail.com id est laborum.'''


res=regex.findall("\w+@+\w+[.]+com",s)
print(res)





# endswith and starts with






# # 1.validate aadhar number 12 digits using regex code below:
# import regex
# aadhar_number = input('Enter aadhar number:')
# res = regex.fullmatch(r'[0-9]{12}',aadhar_number)
# if res:
#     print('valid aadhar number')
# else:
#     print('invalid aadhar number')


# # 2 check if string contains only lower case letters
# s='string'
# res=regex.fullmatch(r'[a-z]+',s)
# if res:
#     print('string contains only lower case letters')
# else:
#     print('string does not contain only lower case letters')

# # 3.check if string contains only upper case letters
# s='STRING'
# res=regex.fullmatch(r'[A-Z]+',s)
# if res:
#     print('string contains only upper case letters')
# else:
#     print('string does not contain only upper case letters')



# 3 validate roll number like CS2024-101
S='CS2024-101'
res=regex.fullmatch('CS[0-9]{4}-[0-9]{3,}',S)
if res:
    print('valid roll number')  
else:
    print('invalid roll number')


#6.COUNT VOWELS USING REGEX
s='VALIDATE'
res=regex.findall('[aeiouAEIOU]',s)
print(len(res))

# 7 replace all digits with *
s1='python program hello123'


res=regex.sub('[0-9]','*',s1)
print(res)


# "*" 0 or more than 0 times
res=regex.fullmatch('ab*c','ac')
if res:
    print('match')
else:
    print('not matched')

# '+' 1 or more than one

res=regex.fullmatch('ab+c','ac')
if res:
    print('match')
else:
    print('not matched')
    

# '?'  0 or 1 times only 
res=regex.fullmatch('ab?c','ac')
if res:
    print('match')
else:
    print('not matched')



# {5,6} 
res=regex.fullmatch('ab{5,6}c','abbbbbbcc')
if res:
    print('match')
else:
    print('not matched')
# {5}
res=regex.fullmatch('ab{5}c','abbbbbc')
if res:
    print('match')
else:
    print('not matched')

[12]
# [1-9] from 1 to 9
res=regex.fullmatch('ab[1-9]c','ab5c')
if res:
    print('match')



# pan card validation
pan_number = input('Enter pan number:')
res = regex.fullmatch('[A-Za-z]{5}[0-9]{4}[A-Za-z]$',pan_number)
if res:
    print('valid pan number')
else:
    print('invalid pan number')


"+91"
res=regex.fullmatch('\+91 [6-9][0-9]{9}','+91 7842259549')   
if res:
    print('valid phone number')
else:
    print('invalid phone number')


# date format 'dd-mm-yyyy'
date = input('Enter date :')
res = regex.fullmatch('([0-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-[0-9]{4}',date)
if res:
    print('valid date')
else:
    print('invalid date')

# remove special characters from string
s='python@program#hello$'
res=regex.sub('[A-Za-z0-9]','',s)
print(res)


