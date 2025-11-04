# # #input is list1=['ccc','bb','a','dddd']
# # #output is list2={3:'ccc',2:'bb',1:'a',4:'dddd'}
# # list1=['ccc','bb','a','dddd']
# # dict2={}
# # for word in list1:
# #     count=0
# #     for char in word:
# #         count+=1
# #     dict2[count]=word
# # print(dict2)    
# # list2=[]
# # #{3: 'ccc', 2: 'bb', 1: 'a', 4: 'dddd'} this dict2 should convert into list2=['a','bb','ccc','dddd']











# # #now output is dict2={a,bb,ccc,dddd}
# # count1=0
# # for i in dict2:
# #     count1+=1
# #     for i in range(1,count1+1):
# #         list2+=dict2[i]
# # print(list2)



# # #lcm and gcd of two numbers using while loop and temporary variable
# # num1=int(input('enter first number:'))
# # num2=int(input('enter second number:'))
# # temp1=num1
# # temp2=num2

# # while temp2!=0:
# #     remainder=temp1%temp2
# #     temp1=temp2
# #     temp2=remainder
# # gcd=temp1
# # lcm=(num1*num2)//gcd
# # print("GCD is:",gcd)
# # print("LCM is:",lcm)






# # def gcd(a,b):
# #     while b:
# #         a,b=b,a%b
# #     return a
# # def lcm(a,b):
# #     return (a*b)//gcd(a,b)
# # num1=int(input('enter first number:'))
# # num2=int(input('entersecond  number:'))
# # print("GCD is:",gcd(num1,num2))
# # print("LCM is:",lcm(num1,num2))


# #removing spaces from given input string
# str1=' Hello  Everyone    how   are youu !'
# str2=''
# for char in str1:
#     if char!=' ':
#         str2+=char
# print(str2)

# #find nearest prime number to a given number 
# num=int(input('enter a number:'))
# low=0
# high=0
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n+1):
#         if n%i==0:
#             return False
#     return True
# a=num-1
# b=num+1
# while True:
#     if is_prime(a):
#         low+=1
#         print(a)
#         break
#     if is_prime(b):
#         high+=1
#         print(b)
#         break
#     a-=1
#     b+=1
#     if low<high:
#         print("nearest prime is:",a)
#         break
#     else:
#         print("nearest prime is:",b)
#         break

fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
# print("Removed:", removed_item)
print("Updated list:", fruits)