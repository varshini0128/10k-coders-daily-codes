#Functions: It is a block of code which is used to perform qa certain action 
#it can be run by calling it 
#SYNTAX: def func_name(parameters)
#types : built in functions, user defined functions
#user defined :

#function to add two numbers
# def add_num():
#     num1=int(input('Enter a number: '))
#     num2=int(input('Enter another number: '))
#     print(num1+num2)
# print('This is first function call ')
# add_num()

# print('This is second function call ')
# add_num()

#a function with parameters 
#we use parameters to pass values into a function while function calling.
def greet():
    print('''Hello Student, thank you for registering at 10K coders, Hope you
          do well in your program''' )
greet()

def greet1(name,program_name):
    print(f'''Hello {name}, thank you for registering at 10K coders, Hope you
          do well in your {program_name}''' )
greet1('varsh','python full stack')

#fun declaration without defining it :
def fun():
    pass

