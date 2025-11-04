# # list1=[]
# # for i in range (10,21):
# #     if i%2==0:
# #         list1+=[i]
# # print(list1)
    
# # # dict1={'name':'varsh','name':'varshini'}
# # # print(dict1)
# # # name=123
# # # rev=0
# # # for i in name:
    

# # # print(rev)

# # num = int(input("Enter a number: "))
# # rev = 0

# # while num > 0:
# #     digit = num % 10
# #     rev = rev * 10 + digit
# #     num = num // 10
# # print("Reversed:", rev)
# # if rev==num:
# #      print('palindrome')
# # else:
# #      print('not a palindrome')


# # num = 125
# # total = 0

# # while num > 0:
# #     digit = num % 10
    
# #     total =total+digit
# #     num = num // 10
    
# # print("Sum of digits is:", total)

# # num=121
# # temp=num
# # rev=0
# # while temp>0:
# #         digit = temp % 10
# #         rev = rev * 10 + digit
# #         temp = temp // 10
# # print(num)
# # if rev==num:
# #     print('palindrome')
# # else:
# #     print('not a palindrome')


# num=6
# for i in range(1,num+1):
#     for j in (num):
#        if num%i==0:
#           print('not prime')
#        else:
#         print(num, 'is prime')



def wait_for_correct_number():
    while True:
        num = int(input("Enter a number greater than 10: "))
        
        if num > 10:
            print("✅ Condition met! Exiting loop...")
            break
        else:
            print("❌ Condition failed. Try again...")
wait_for_correct_number()
