# OOPS: OBJECT ORIENTED PROGRAMMING LANGUAGE
# OOPs is a obj oriented programming system is a programming paradigm it contains 
#data and code manipulate data is known as oops
#paradigm: a programming paradigm is a fundamental style of computer programing that provides a structure and approach to solve problems 
# paradigm is nothing but solving one task in multiple approaches like loops or functions or classes
#python is a multi paradigm programming language
#oops advantages
        # code reusability
        #improve maintainability
        #data security




def details():
    name='kumar'        #local variables
    pin=101

def H():
    # print(name)      error because accessing out of scope variable
    # print(pin)
    print("Hi")
H()
#in oops we call functions as methods and variables as attributes
# class is blueprint of object or template for creating objects it defines attributes (variables  ) and methods (functions)
# that describes the behavior and state of the objects 
# objects are the instances of classes
# syntax for creating class and obj
# class first:
        #class body
#obj=first()
class String:
    def user_swapcase(self,a):
        res=''
        for x in a:
            if ord(x)>=65 and ord(x)<=90:
                h=ord(x)+32
                res+=chr(h)
            elif ord(x)>=95 and ord(x)<=122:
                h1=ord(x)-32
                res+=chr(h1)
        print(res)
obj=String()
obj.user_swapcase('pyTHoN')



class first:
    def __init__(self):   #a-z it is a constructor it constructs an object for calling constructor we just need to create an object for this constructor because 
        print('object oriented programming or oops')

obj=first()


#constructor is a special method in python
class second:
    def __init__(self):     #constructor
        print("python")
    def method1(a):
        print('this is method')

obj=second()  #we need to create and object and refer the method from class
obj.method1()


class A:
    def method(self,name):
        self.name=name
        print("My name is :",name)

#we can create no of objects for one class
obj1=A()
obj1.method('kumar')
obj2=A()
obj2.method('ajay')
obj3=A()
obj3.method('ravi')


print(obj2.name)
print(obj3.name)
print(obj1.name)

#instance method : it contains self as  first parameter 

#parameter less constructor:
class Test:
    def __init__(self):
        self.name='kumar'       #instance variables 
        self.emp_id = 101
        print(self.name)
        print(self.emp_id)

obj = Test()

#parameterised constructors:
class Test1:
    def __init__(self,name,emp_id,salary):
            self.name=name       #instance variables 
            self.emp_id = emp_id
            self.salary=salary
    def method1(self):
            print("name is ",self.name)
            print('emp id is ',self.emp_id)
            print("employee salary is ",self.salary)

obj = Test1('kumar',101,80000)
obj2 = Test1('sai',102,45000)
obj.method1()


#types of variables
        #instance variable : declared with self  and declared inside constructor 
        # and instance method by using self variable.
        # outside of the class using object reference



# instance variable declaring in instance method by using self variable.
class C:
    def __init__(self):
        self.name='ravi'
    def details(self):  #instance method
        self.pin=101

    def method2(self):
        self.salary=8000

obj=C()
obj.details()
obj.method2()

print(obj.__dict__)


 # outside of the class using object reference
class D:
    def __init__(self):
        self.name='ravi'
    def details(self):  #instance method
        self.pin=101


obj=D()
obj.details()
obj.salary=9000
print(obj.__dict__)

"how to access instance variables"
class K:
    def __init__(self):
        self.name='ravi'
    def details(self):  #instance method
        self.pin=101
        self.salary=8000
    def display(self):
        print(self.name)
        print(self.pin)
        print(self.salary)

obj=K()
obj.details()
# obj.method2()


# access
print(obj.name)
print(obj.pin)
print(obj.salary)
print(obj.__dict__)



class Bank:
    def create_account(self,acc_no,balance,name):
        self.acc_no=acc_no
        self.balance=balance
        self.name=name
    def display(self):
        print(self.acc_no)
        print(self.balance)
        print(self.name)
obj=Bank()
obj.create_account(109876543,50,'varshini')
obj.display()

class Bank1:
    def create_account(self):
        self.Acc_no=int(input('enter account number'))
        self.balance=int(input('enter balance'))
        self.name=input('enter name ')
    def display(self):
        print(self.Acc_no)
        print(self.balance)
        print(self.name)
obj=Bank1()
obj.create_account()
obj.display()


class Test2():
    def __init__(self):
        self.balance=10000

    def method1(self):
        self.balance=4000
        print(self.balance)
obj=Test2()
obj.method1()
print(obj.balance)

"static or class"
class E():
    salary=3400
    def method(cls):
        cls.name='mohan'
obj=E()
print(E.__dict__)
        
