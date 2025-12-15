# # OOPS: OBJECT ORIENTED PROGRAMMING LANGUAGE
# # OOPs is a obj oriented programming system is a programming paradigm it contains 
# #data and code manipulate data is known as oops
# #paradigm: a programming paradigm is a fundamental style of computer programing that provides a structure and approach to solve problems 
# # paradigm is nothing but solving one task in multiple approaches like loops or functions or classes
# #python is a multi paradigm programming language
# #oops advantages
#         # code reusability
#         #improve maintainability
#         #data security
          #scalability
          #enhanced code readability
#features of oops"
        #class      #blueprint of object
        #object     #instance of a class
        #encapsulation
        #inheritance
        #polymorphism
        #abstraction 


#types of variables:
        # instance variable
        # local variable
        # static /class variable
# instance variable:
            # inside instance , constructor and outside class
class school:
    def teach(self):
        self.school_name = 'pragathi'
        self.pin=789
        std_age=22  #local variable
obj=school()
print(obj.__dict__)

#inside constructor
class employee:
    def __init__(self):
        self.emp_name='ravi'    #instance variables
        self.id=90
        self.salary=90000

obj=employee()
print(obj.__dict__)

# outside class
class tenk:
    def sale_dep(self):
        self.name='mohan'
obj=tenk()
obj.sale_dep()
obj.salary=900
obj.age=21              #instnace variable outside the class
print(obj.__dict__)

# where to delete instance variables:
#                       inside instance method,inside constructor , outside class
# inside instance method:
class k:
    def __init__(self):
        self.name='mohan'
    def instance_method(self):
        del self.name
        print('after delete')
        print(self.name)            #attribute error
obj=k()
obj.instance_method()

#inside constructor:
class school1:
    def __init__(self):
        self.HM='arjun'     #instance variable
        self.name='mohan'
        print(self.HM)
        del self.HM
        print('after delete')
        print(self.HM)          #attribute error

obj=school1()
print(obj.__dict__)

#  outside class
class school2:
    def __init__(self):
        self.HM='arjun'     #instance variable
        self.name='mohan'
        print(self.HM)
              

obj=school2()
del obj.HM          #it is deleted only in this object if we create another obj and print it will b printed
print(obj.__dict__)


#where to print instance variables  
                    # inside instance method,inside constructor , outside class, subclass/child class
class emp:
    def __init__(self):
        self.emp_name='ravi'
        self.id=90
        self.salary=98009
        self.dept='IT'
        print('employee name is : ', self.emp_name)         #inside constructor
        print('employee id is : ', self.id)
    def instance_method(self):
        print('employee salary is : ', self.salary)         #inside class
        print('employee dept is : ', self.dept)


obj=emp()
obj.instance_method()

print(obj.emp_name)     #outside class
print(obj.salary)
print(obj.id)
print(obj.dept)


class manager(emp):
        def method(self):
            print(self.emp_name)        #inside a subclass or child class
            print(self.id)
obj=manager()
obj.method()


# how to update instance variables: 
                        # inside instance method,inside constructor , outside class
class school3:
    def __init__(self):
        self.value1=500
    def instance_method(self):
        self.value1+=500
obj=school3()
obj.instance_method()
print(obj.__dict__)
print()

obj2=school3()
print(obj2.__dict__)

obj2.value1+=59
print(obj2.__dict__)


"static/class variable"
"can be declared inside class outside method"


class Bank:
    balance=10000           #static or class variable
    def create_acc(self):
        self.holder_name='kumar'
print(Bank.__dict__)
print("=====instance variable=========")
obj=Bank()
obj.create_acc()
print("holder name: ",obj.holder_name)


"instance method"
class Emp:
    def instance_method(self):
        self.name='kitu'        #instance variable 
        Emp.name1='kittuu'      #class variablee
obj=Emp()
obj.instance_method()
print(Emp.__dict__)


# inside class method
class employees:
    def __init__(self):
            self.pin=90     #instance variable
            employees.salary=89000  #class variable 
    @classmethod
    def create_account(cls):
        cls.name='ravi'         #class variable

employees.create_account()
print('======obj========')
obj=employees()
obj.create_account()

#declaring class variable outside class 
class bank:
    def method(self):
        pass
bank.hname='tirtir'         #class variable
bank.pin=90
print(bank.__dict__)


#print class variables

class A :
    ename='kumar'       #class variable
    def method(self):           #printiing inside instance method
        print(A.ename)          #we can also use self for printing 
    def __init__(self):         #printing inside constructor
        print(A.ename)
obj=A()
obj.method()

#printing inside class method
class school:
    name='pratibha'
    @classmethod
    def cls_method(cls):
        print(cls.name)     #using method self->cls parameter
        print(school.name)      #using cls name

school.cls_method()
print(school.name)      #using cls name outside class


#update class variable 

class bank1:
    balance=9000
    def instance_method(self):
        self.balance+=500
obj1=bank1()
obj1.instance_method()
print(obj.__dict__)


"class method"
# class bank2:
#     balance=1002        #class variable
#     @classmethod
#     def cls_method(cls):
#         cls.balance+=2345


#del cls variable













#local variables 
        # 'we can declare inside class ,class method, constructor, instance method'
class employeee:
    def instance_meth(self):
        name='kumar'        #local variable cant be printed outside the class
        pin=909
        print(name)

obj=employeee()
obj.instance_meth()
# print(obj.name) we get error cozz local variable cant be printed outside the class
'inside class method'
class emp2():
    @classmethod
    def cls_method1(cls):
        sal=90009
        print(sal)

obj=employeee()
obj.cls_method1()


class emp():
    def __init__(self):
        self.emp_name='sai'
    @staticmethod
    def static_method():
        # print(self.emp_name)  we cant call 
        e_name='sai'
        e_id=90
        e_salary=898989
    def instance_method(self):
        # print(e_name)
        # print(e_id)
        # print(e_salary)    we get error cant call local in instance
        print('=========')
obj=emp()
obj.static_method()
obj.instance_method()






# def details():
#     name='kumar'        #local variables
#     pin=101

# def H():
#     # print(name)      error because accessing out of scope variable
#     # print(pin)
#     print("Hi")
# H()
# #in oops we call functions as methods and variables as attributes
# # class is blueprint of object or template for creating objects it defines attributes (variables  ) and methods (functions)
# # that describes the behavior and state of the objects 
# # objects are the instances of classes
# # syntax for creating class and obj
# # class first:
#         #class body
# #obj=first()
# class String:
#     def user_swapcase(self,a):
#         res=''
#         for x in a:
#             if ord(x)>=65 and ord(x)<=90:
#                 h=ord(x)+32
#                 res+=chr(h)
#             elif ord(x)>=95 and ord(x)<=122:
#                 h1=ord(x)-32
#                 res+=chr(h1)
#         print(res)
# obj=String()
# obj.user_swapcase('pyTHoN')



# class first:
#     def __init__(self):   #a-z it is a constructor it constructs an object for calling constructor we just need to create an object for this constructor because 
#         print('object oriented programming or oops')

# obj=first()


# #constructor is a special method in python
# class second:
#     def __init__(self):     #constructor
#         print("python")
#     def method1(a):
#         print('this is method')

# obj=second()  #we need to create and object and refer the method from class
# obj.method1()


# class A:
#     def method(self,name):
#         self.name=name
#         print("My name is :",name)

# #we can create no of objects for one class
# obj1=A()
# obj1.method('kumar')
# obj2=A()
# obj2.method('ajay')
# obj3=A()
# obj3.method('ravi')


# print(obj2.name)
# print(obj3.name)
# print(obj1.name)

# #instance method : it contains self as  first parameter 

# #parameter less constructor:
# class Test:
#     def __init__(self):
#         self.name='kumar'       #instance variables 
#         self.emp_id = 101
#         print(self.name)
#         print(self.emp_id)

# obj = Test()

# #parameterised constructors:
# class Test1:
#     def __init__(self,name,emp_id,salary):
#             self.name=name       #instance variables 
#             self.emp_id = emp_id
#             self.salary=salary
#     def method1(self):
#             print("name is ",self.name)
#             print('emp id is ',self.emp_id)
#             print("employee salary is ",self.salary)

# obj = Test1('kumar',101,80000)
# obj2 = Test1('sai',102,45000)
# obj.method1()


# #types of variables
#         #instance variable : declared with self  and declared inside constructor 
#         # and instance method by using self variable.
#         # outside of the class using object reference



# # instance variable declaring in instance method by using self variable.
# class C:
#     def __init__(self):
#         self.name='ravi'
#     def details(self):  #instance method
#         self.pin=101

#     def method2(self):
#         self.salary=8000

# obj=C()
# obj.details()
# obj.method2()

# print(obj.__dict__)


#  # outside of the class using object reference
# class D:
#     def __init__(self):
#         self.name='ravi'
#     def details(self):  #instance method
#         self.pin=101


# obj=D()
# obj.details()
# obj.salary=9000
# print(obj.__dict__)

# "how to access instance variables"
# class K:
#     def __init__(self):
#         self.name='ravi'
#     def details(self):  #instance method
#         self.pin=101
#         self.salary=8000
#     def display(self):
#         print(self.name)
#         print(self.pin)
#         print(self.salary)

# obj=K()
# obj.details()
# # obj.method2()


# # access
# print(obj.name)
# print(obj.pin)
# print(obj.salary)
# print(obj.__dict__)



# class Bank:
#     def create_account(self,acc_no,balance,name):
#         self.acc_no=acc_no
#         self.balance=balance
#         self.name=name
#     def display(self):
#         print(self.acc_no)
#         print(self.balance)
#         print(self.name)
# obj=Bank()
# obj.create_account(109876543,50,'varshini')
# obj.display()

# # class Bank1:
# #     def create_account(self):
# #         self.Acc_no=int(input('enter account number'))
# #         self.balance=int(input('enter balance'))
# #         self.name=input('enter name ')
# #     def display(self):
# #         print(self.Acc_no)
# #         print(self.balance)
# #         print(self.name)
# # obj=Bank1()
# # obj.create_account()
# # obj.display()


# class Test2():
#     def __init__(self):
#         self.balance=10000

#     def method1(self):
#         self.balance=4000
#         print(self.balance)
# obj=Test2()
# obj.method1()
# print(obj.balance)

# "static or class"
# class E():
#     salary=3400
#     def method(cls):
#         cls.name='mohan'
# obj=E()
# print(E.__dict__)
        
# #day3 dec3

# class Test3:
#     class_variable=1000         #class variable declared in class and outside of method
#     def method(self):
#         self.name='python'  #instance method
#         Test3.name='pyth'   #class variable
# obj=Test3()
# obj.method()
# print(Test3.__dict__)

# class Test4:
#     @classmethod
#     def classmethod3(cls):      #class method
#         cls.value=2500
# Test4.classmethod3()
# print(Test4.__dict__)
# print()
# print()
# obj=Test4()
# obj.classmethod3()
# print(Test4.__dict__)


# #how to access class variable
# class G:
#     balance=9000
#     def __init__(self):
#         print(G.balance)
#     def method(self):
#         print(G.balance)
# obj=G()
# obj.method()
# print(G.balance)
# print(obj.balance)

# # #how to update class variable
# class Test5():
#     balance=80

#     @classmethod
#     def cls_method(cls):
#         cls.balance+=20
#         print(Test5.balance)
        

    


# # dec5
# # inheritance: it is a feature in oops where child class inherits the prop and behaviors of a parent class
# # types
# #1 single-level inheritance: one child inherits from one parent class ex: one-to-one
# #2 multiple inheritanc: one child inherits from multiple parent classes ex many-to-one
# #3multi-level inhertance one child inherits from one parent other child inherits from that child ex: chain
# #4 heirarchical inheritance:
# #5 


# # 1 single-level inheritance
# class parent:
#     def parent_method(self):
#         self.parent_name=input('enter parent name:')
#         self.parent_age=int(input('enter parent age: '))

# class child(parent):
#     def child_method(self):
#         self.c_name=input("enter child name: ")
#         self.c_age=int(input("enter child age: "))
#     def details(self):
#         print('parent name',self.parent_name)
#         print('parent age:',self.parent_age)
#         print("=======child========")
#         print("child name",self.c_name)
#         print('child age',self.c_age)

# p_obj=parent()
# p_obj.parent_method()



# ch_obj=child()
# ch_obj.parent_method()
# ch_obj.child_method()
# ch_obj.details()



# # multi-level inheritance: one child from other child

# class g_father:
#     def g_fathermethod(self):
#         self.g_name='ravi'
#         self.g_age=80
# class father(g_father):
#     def father_method(self):
#         self.fathername='mohan'
#         self.father_age=50
# class child(father):
#     def child_mehtod(self):
#         self.c_name='ajay'
#         self.c_age=20
#     def details(self):
#         print('=======grandfather=========')
#         print(self.g_name)
#         print(self.g_age)
#         print('=======father=========')
#         print(self.fathername)
#         print(self.father_age)
#         print('=======child=========')
#         print(self.c_name)
#         print(self.c_age)

# c_obj=child()
# c_obj.g_fathermethod()
# c_obj.father_method()
# c_obj.child_mehtod()
# c_obj.details()




# multiple inheritance:

class parent1:
    def __init__(self):
        self.p1_name='ram'
    def method1(self):
        self.p1_age=int(input('enter p1 age: '))
class parent2:
    def __init__(self):
        self.p2_name='ravi'
    def method2(self):
         self.p2_age=int(input('enter p2 age:'))
        
class parent3:
    def __init__(self):
        self.p3_name='ramu'
    def method3(self):
            self.p3_age=int(input("enter p3 age:"))

class child1(parent1,parent2,parent3):
    def __init__(self):
        self.child_name='varsh'
        super().__init__(self)
        parent1.__init__(self)
        parent2.__init__(self)
        parent3.__init__(self)
    def child1_method(self):
        self.child_age=(input('enter child age'))
    def details(self):
        print("===========parent1============")
        print(self.p1_age)
        print(self.p1_name)
        print("===============parent2============")
        print(self.p2_age)
        print(self.p2_name)
        print("===========parent3============")
        print(self.p3_age)
        print(self.p3_name)
        print("===============child============")
        print(self.child_age)
        print(self.child_name)
obj=child1()
obj.method1()
obj.method2()
obj.method3()
obj.child1_method()
obj.details()


# 10 dec
#mro==>method revolution order
class A:

    def work(self):
        print('this is class A')
class B:
    def work(self):
        print("this is class B")
class child(A,B):
    pass
obj=child()
obj.work()
print(child.mro())

'multi level inheritance'
class A :
    def method1(self):
        self.name='kumar'
        print('this is class A')
class B(A):
    def method2(self):
        print('this is class B')
class C(B):
    def method3(self):
        print('this is class C')
obj=C()
obj.method1()
obj.method2()
obj.method3()
print(obj.name)



'heirarchical inheritance'
                        #multiple childs inherits from only one parent class
class parent:
    def __init__(self):
        self.parent_name='ravi'
        self.parent_age=39
class child1(parent):
    def ch_method(self):
        self.ch_name='sarika'
        self.ch_age=22
class child2(parent):
    def ch_method2(self):
        self.ch2_name='latha'
        self.ch2_age=21
class child3(parent):
    def ch_method3(self):
        self.ch3_name='hema'
        self.ch3_age=20

obj = child3()
print('parent details: ')
print(obj.parent_name)
print(obj.parent_age)
print('child3 details')
obj.ch_method3()
print(obj.ch3_name)
print(obj.ch3_age)


obj=child2()
obj.ch_method2()
print('child2 details')
print(obj.ch2_name)
print(obj.ch2_age)



#abstraction:
                #ABSTRACTION is one of the fundamental concept in oops, it means hiding internal implemenatation
                # details and showing only essential features
                # example : atm machine ==> 
                # abstraction  methods is known as abstract class 

@classmethod
def method(cls):
    pass
@staticmethod
def method():
    pass
from abc import ABC,abstractmethod

class abstract_class(ABC):
    @abstractmethod
    def abc_method(self):
          pass
    @abstractmethod
    def method(self):
        pass
# obj=abstract_class()      we cant create and call object for abstract classand method
# obj.abc_method()




