# # class A():
# #     def __init__(self):
# #         self.item1=100
# #     def method(self):
# #         self.name='ravi'
# #         self.item1+=290
# #         del self.name
# #         # print(self.name)
# # obj=A()
# # obj.method()
# # print(obj.__dict__)
# # print(obj.item1)




# #up del print
# # class student:
# #     student1='varsh'
# #     std_id=21
# #     std_dept='cse'
# #     pin=90
# #     item=30
# #     @classmethod
# #     def cls_method(cls):
# #         cls.std_dept='aiml'
# #         cls.student1+='ini'
# #         print(cls.std_dept)
# #         del student.pin
# #     def method(self):
# #         self.std_id=9
# #         print(self.std_id)

# # obj=student()
# # obj.method()
# # print(obj.__dict__)
# # print(student.std_id)
# # print(student.std_dept)
# # obj.cls_method()
# # print(student.std_dept)
# # print(student.student1)
# # print(obj.__dict__)
# # print(student.__dict__)
# # del student.item
# # print(student.__dict__)

# # import random

# # while True:
# #     user_input=int(input('guess a number: '))
# #     r= random.randint(1,4)
# #     if user_input==r:
# #         print('your guess correct',user_input)
# #         break
# #     else:
# # #         print('try again')



# # # # while loop:

# # # n=input('enter your password')
# # # while n!='Ajay@123':
# # #     n=input('enter password:')
# # # print('password',n)

# # # multiplication table
# # a=1
# # n=2
# # while a<=10:
# #     print(n,'x',a ,'=',n*a)
# #     a+=1
    
# # k=789
# # s=0
# # while k>0:
# #     d=k%10
# #     s+=d
# #     k//=10
# # print(s)

# #sum of even numbers
# k=23568
# sum=0
# while k>0:
#     d1=k%10
#     if d1%2==0:
#         sum+=d1
#     k//=10
# print(sum)
    

# #sum of prime 
# n=2345678
# sum_of_even=0
# while n>0:
#     d=n%10
#     count=0
#     for i in range(1,d+1):
#         if d%i==0:
#             count+=1
#     if count==2:
#         sum_of_even+=d
#     n//=10


# for i in range(1,5):
#     for j in range(1,5):
#         if j==1 or i==1 or j==4 or i==4:
#             print('*',end=" ")
#         else:
#             print(" ",end=" ")
#     print()


def add(a,b):
    print(a+b)
print(type(add(7,9)))

# def sub(a,b)