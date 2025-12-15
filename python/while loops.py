# # # while loops
# # j=2345
# # l=j
# # res=0
# # while j>0:
# #     d=j%10
# #     res=res*10+d
# #     j//=10
# # print(res)

# # if l==res:
# #     print('palindrome')
# # else:
# #     print('not palindrome')


# # #length of a number
# # k=1238765
# # count=0
# # list1=[]
# # while k>0:
# #     d=k%10
# #     if d%2==0:
# #       count+=1
# #     #   print(d)
# #       list1.append(d)
# #     k//=10
# # print(count)
# # print(list1)


# #strong number 
# l=145
# j=l
# sum=0
# while l>0:
#     d1=l%10
#     f=1
#     for i in range(1,d1+1):
#         f*=i
#     sum+=f
#     l//=10
# print(sum)            
# if sum==j:
#     print('strong number')
# else:
#     print('not a strong number')


# #print all even numbers from 1 to 100 using while 
# a=1
# l1=[]
# while a<=100:
#     if a % 2 ==0:
#         l1.append(a)
#     a+=1
# print(l1)

#sum of all numbers between 1 and N user input 
# a=1
# n=int(input('enter number'))
# sum=0
# while a <= n:
#     sum+=a
#     a+=1
# print(sum)
    
#count the no of digits in given number using while
p=12345
count1=0
while p>0:
    d=p%10
    count1+=1
    p//=10
print(count1)

#reverse the digits of a given number
a=12345


