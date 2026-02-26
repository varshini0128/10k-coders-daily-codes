# # print(10/0) zerodivision error

# # # print(10+'python') type error

# # print(10/1)
# # print(10/2)
# # print(10/3)
# # # print(10/0)  #exception 
# # print(10/5)
# # print(10/6)

# # exception handling: is a mechanism to handle runtime errors in a controlled manner.
# #  It allows us to write code that can handle errors without crashing the program.


# # four blocks of exception handling:
# # 1. try block: contains code that may raise an exception.
# # try is a key word in python the main objective of try is to put all risky code inside try block and if any exception occurs in try block then it will be handled by except block and if no exception occurs then else block will be executed and finally block will be executed regardless of whether an exception occurs or not.


# # 2. except block: contains code that will be executed if an exception occurs in the try block.
# # What is Exception Handling?
# # Exception Handling is a mechanism to handle runtime errors gracefully so that the program does
# # not crash.
# # It is done using:
# # try, except, else, finally


# # 3. else block: contains code that will be executed if no exception occurs in the try block.


# # 4. finally block: contains code that will be executed regardless of whether an exception occurs or not.



# 'types of errors'
# # 1. Syntax Error: occurs when the code is not written in the correct syntax.
# # 2. Runtime Error: occurs when the code is syntactically correct but an error
# # occurs during execution.
# # 3. Logical Error: occurs when the code is syntactically correct and runs without
# # errors but produces incorrect results.
# # 4. Semantic Error: occurs when the code is syntactically correct and runs without
# # errors but produces incorrect results due to incorrect logic or meaning of the code.
# # NameError = occurs when a variable is not defined.

# try:
#     a=10
#     # print(h) after this line execution stops because h is not defined and it will raise a NameError
#     print(a)
#     print(b)
# except NameError as e:
#     print("NameError occurred:", e)

# # zeroDivisionError = occurs when we try to divide a number by zero.
# try:
#     a=10
#     b=0
#     print(a/b)
# except ZeroDivisionError as e:
#     print("ZeroDivisionError occurred:", e)



# # typeError = occurs when we try to perform an operation on incompatible data types.
# try:
#     a=10
#     b='python'
#     print(a+b)
# except TypeError as e:
#     print("TypeError occurred:", e)



# print(int('100'))

# # valueError = occurs when we try to convert a string that cannot be converted to an integer.
# try:    
#     a='python'
#     print(int(a))
# except ValueError as e:
#     print("ValueError occurred:", e)



# 9/2/2026
# # SyntaxError = occurs when the code is not written in the correct syntax.
# try:
#     for i in range(5)
#         print(i)
# except SyntaxError as e:
#     print("SyntaxError occurred:", e)

# # we cant catch syntax error using try except because syntax error occurs when the code is being parsed and it will not be executed at all so we cant catch it using try except block.


# # index error = occurs when we try to access an index that is out of range.
# try:
#     a=[1,2,3]
#     print(a[5]) 
# except IndexError as e:
#     print("IndexError occurred:", e)


# # fileNotFoundError = occurs when we try to open a file that does not exist.
# try:    
#     f=open('file.txt','r')      

# except FileNotFoundError as e:
#     print("FileNotFoundError occurred:", e)


# # 'default exceptions in python'
# # they are declared at last 
# except:
#     print("An error occurred")


# try:
#     print('outside try block')
#     try:
#         print('inside try block')
#     except:
#         print('inside except block')
#     else:
#         print('inside else block')
#     finally:
#         print('inside finally block')
# except:
#     print('outside except block')
# else:
#     print('outside else block') 
# finally:
#     print('outside finally block')





# import keyword
# print(keyword.kwlist)
# # print(r)


23/2/2026
import pickle 
l=[101,'hari',22000]
with open('pickle741.pkl','wb') as k:
    pickle.dump(l,k)


emp ={
'emp_pin':101,
'emp_name':'sai',
'emp_salary':25000
}
with open('pickle741.pkl','wb') as k:
    pickle.dump(emp,k)

class students:
    def __init__(self,std_id,std_name,std_age):
        self.std_id = std_id
        self.std_name = std_name
        self.std_age = std_age

with open('pickle741.pkl','wb') as k:
    s1 = students(101,'sai',15)
    pickle.dump(s1,k)

with open('pickle741.pkl','rb') as h:
    data = pickle.load(h)
    print(data)

class employee:
    def __init__(self):
        self.emp_pin = 101
        self.emp_name = 'sai'
        self.emp_salary = 25000
    def employe_rec(self):
        print('Employee Pin:',self.emp_pin)
        print('Employee Name:',self.emp_name)
        print('Employee Salary:',self.emp_salary)

with open('pickle741.pkl','wb') as k:
    e1 = employee()
    pickle.dump(e1,k)

with open('pickle741.pkl','rb') as h:
    data = pickle.load(h)
    data.employe_rec()


# 'zip folder'
# from zipfile import *
# zipfolder=ZipFile('myzip.zip','w',ZIP_DEFLATED)
# zipfolder.write('pickle741.pkl')
# zipfolder.write('abc.py')
# zipfolder.write('abc.txt')

# read=ZipFile('myzip.zip','r',ZIP_STORED)
# d=read.namelist()
# print(d)
# # read.extractall('myzip') or
# for x in d:
#     b=open(x,'r')
#     print(b.read())


'generator function'
def gen():
    for x in range(5):
        yield x

g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

a=10
b=22
print(a+b*2)


with open('abc.py','r') as h:
    print(h.read())


# between prime using generator function
def prime_gen(n):
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield num
n = 20
for prime in prime_gen(n):
    print(prime)
