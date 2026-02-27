
# '27/02/2026'
import time

import threading

# def even():
#     for x in range(10,20):
#         if x%2==0:
#             time.sleep(1)
#             print('even:',x)


# def odd():
#     for x in range(10,20):
#           if x%2==1:
#             time.sleep(1)
#             print('odd:',x)


# # start_time=time.time()

# # even()
# # # odd()
# # # end_time=time.time()
# # # t_time=end_time-start_time
# # # print(t_time)

# # t1=threading.Thread(target=even)
# # t2=threading.Thread(target=odd)

# # t1.start()
# # t2.start()

# # t1.join()
# # t2.join()



# # def even(a,b):
# #     for x in range(a,b):
# #         if x%2==0:
# #             time.sleep(1)
# #             print('even:',x)


# # def odd(a,b):
# #     for x in range(a,b):
# #           if x%2==1:
# #             time.sleep(1)
# #             print('odd:',x)


# # t1=threading.Thread(target=even,args=(10,20))
# # t2=threading.Thread(target=odd,args=(10,20))

# # t1.start()
# # t2.start()

# # t1.join()
# # t2.join()


# # 1.multithreading using class(Bank Example)
# class Bank():
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
    
#     def withdraw(self,amount):
#         if self.balance>=amount:
#             print('withdrawn amount:',amount)
#             self.balance=self.balance-amount
#             time.sleep(1)
#             print('available balance:',self.balance)
#         else:
#             print('insufficient balance')
#     def check_balance(self):
#         time.sleep(1)
#         print('available balance:',self.balance)

# b=Bank('ravi',10000)

# t1=threading.Thread(target=b.withdraw,args=(2000,))
# t2=threading.Thread(target=b.check_balance)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# squares and cube

# def square(a,b):
#     for i in range(a,b):
#      print('square',i**2)
#      time.sleep(1)

# def cube():
#     for i in range(1,10):
#      print('cube',i**3)
#      time.sleep(1)
   



# t1=threading.Thread(target=square,args=(1,10))
# t2=threading.Thread(target=cube,)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# def num(a,b):
#    for i in range(a,b):
#       print('number',i)
#       time.sleep(1)

# s='string is a python data type'

# def char():
#    for x in s:
#       print('char:',x)
#       time.sleep(1)

# t1=threading.Thread(target=num,args=(1,10))
# t2=threading.Thread(target=char,)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# pos_neg=[1,-2,3,-4,5,-6,7,-8,9,-10]

# def pos():
#    for i in pos_neg:
#       if i>0:
#          print("positive:",i)
#          time.sleep(1)
# def neg():
#    for i in pos_neg:
#       if i<0:
#          print("negative:",i)
#          time.sleep(1)

# t1=threading.Thread(target=pos)
# t2=threading.Thread(target=neg)

# t1.start()
# t2.start()

# t1.join()
# t2.join()



# def pos(a):
#    for i in a:
#       if i>0:
#          print("positive:",i)
#          time.sleep(1)
# def neg(a):
#    for i in a:
#       if i<0:
#          print("negative:",i)
#          time.sleep(1)
# a=[1,-10,2,-9,3,-1,4,-4,5]
# t1=threading.Thread(target=pos,args=(a,))
# t2=threading.Thread(target=neg,args=(a,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# 8. divisible by 3 and 5

# def three():
#    for i in range(1,10):
#       if i%3==0:
#          print('num divisible by 3:',i)
#          time.sleep(1)


# def five():
#    for i in range(1,10):
#       if i%5==0:
#          print('num divisible by 3:',i)
#          time.sleep(1)


# t1=threading.Thread(target=three)
# t2=threading.Thread(target=five)

# t1.start()
# t2.start()

# t1.join()
# t2.join()


" "
def file1():
    with open('file1.txt','r') as k:
        s=k.readlines()
        for x in s:
            time.sleep(1)
            print(x)

def file2():
    with open('file2.txt','r') as k:
        s=k.readlines()
        for x in s:
            time.sleep(1)
            print(x)

t1=threading.Thread(target=file1)
t2=threading.Thread(target=file2)

t1.start()
t2.start()

t1.join()
t2.join()

