#Scoping: It determines the availabilty of an vaariable in functions 
#global variable: These variables are declared outside a function and are available to all  the functions inside a program
gvar='varsh-global var'
def fun1():
    print('this is function 1')
    print(gvar)
    def fun2():
        print('this is nested function')
        def fun3():
            print(gvar)
        fun3()
    fun2()
fun1()

        

# #Non local /Enclosing variable: These are declared inside a nested function
# #it is declared in the outer function of nested function.
# #even though we use same variable name in both inner and outer ffunction,python thinks both variables are different because of their scope.

# def outer_func():
#     var1='varsh-outer func'
#     def inner_func():
#         var2='this is inner function'
#         print(var1)
#     inner_func()
#     print(var1)
# outer_func()

def func1():
    a=10
    b=20
    var=a+b
    print(var)
    def func2():
        a1=2
        b2=3
        var1=a1*b2
        print(var1)
        print(var) #can acces var from outer function
    func2()
    print(var)
    # print(var1)  #gives error cant acces var from inner function in outside function



    


# #local variable: These are only available inside the function in which they are defined 
# #we declare a variable as local when we dont want that data to be accessed by other functions in the program.
# def add():
#     a=10    #local variable: they cant call outside a function
#     b=20
#     print(a+b)
# #print(a)  #gives error because it is not available outside the function.
# add()
# #built in variable

#global keyword: this is used to make changes to a global variable inside a function
x=20
def globdemo():
    global x
    x=15
    print(x)

globdemo()
print(x)

name='varsh'
def globdemo1():
    global name
    name='varshini'
    print(name)
globdemo1()
print(name)

#non local keyword: This is used to make changes to a non local variable inside a local function
def outer():
    var='varsh-outer'
    print(var)
    def inner():
        nonlocal var
        var='varshini-inner'
        print('inner var:',var)
    inner()
    print('outer var:',var)
outer()
#Built in variable : It is a phenomenon where built in function names are used as variable.
#It is illegal to use built in variables as it over rides the functionality of built in functions
len='varsh'
print(len)
# print(len('varshini'))  #gives error because len is used as variable name