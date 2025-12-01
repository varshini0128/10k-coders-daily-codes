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



class second:
    def __init__(self):
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

#instance method : it contains self as a parameter 