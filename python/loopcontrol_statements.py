# # #Loop control statements :
# # #These are used to control the flow of a loop in a program based on a condition
# # #there are three statements
# # #break
# # #continue
# # #pass

# # #break: it is used to break a loop in between of its iteration based on a condition
# # for i in range(1,11):
# #     print(i)
# #     if i==5:
# #         break

# # #continue:


# # #for loop with else: we can a pass a else statement to a loop when the loop executes 

# # names =['sana','sai kiran', 'murthi','sanjana','akshaya','yona']

# # for name in names:
# #     if name=='murthi':
# #         print(name,'found')
# #         break
# # else:
# #      print('Name not found')

# #Task: write a program using while loop such that the loop must break when the user pass the input 0 else it should print the value passed by the user

# Flag=True
# # num1=int(input('enter a number: '))
# while Flag==True:
#     num1=int(input('enter a number: '))
#     if num1==0:
#         print('zero')
#         Flag==False
#         break
#     else:
#         continue

# names =['sana','sai kiran','murthi','sanjana','akshaya','yona']
# val=True
# while val==True:
#     for name in names:
#         if name=='murthi':
#             print('name found')
#             val==False
#             break
#         else:
#             #  print('name not found')
#              continue
#     break


# #userid 


# user_name='admin'
# pw='1234'
# while True:
#     username=input('Enter username: ')
#     if username=='admin':
#         while True:
#              password=input('Enter password: ')
#              if password==pw:
#                 print('login success')
#                 break
#              else:
#                 print('wrong password')
#         break
#             # password=input('Enter password: ')
#             # if password==pw:
#             #     print('login success')
               
             
       
#     else:
#         print('Invalid username')
        

# # # Store username and password
# # username = "varshini"
# # password = "1234"

# # # Keep asking until the correct username is entered
# # while True:
# #     user_input = input("Enter username: ")
    
# #     if user_input == username:
# #         # If username is correct, now check password
# #         while True:
# #             pass_input = input("Enter password: ")
# #             if pass_input == password:
# #                 print("Login successful ✅")
# #                 break  # Exit the password loop
# #             else:
# #                 print("Invalid password. Try again.")
# #         break  # Exit the main loop after successful login
# #     else:
# #         print("Invalid username. Try again.")


# #Continue: It is used to restart an iteration based on a condition
# # It stops an iteration in between and goes for next iteration
# # Difference between break and continue
# # break completely exits the loop whereas xcontinue stops the current iteration and goes for next iteration


# for i in range(1,11):
#     if i%2!=0:
#         continue
#     print(i)


# #task : write a number

# for i in range(1,6):
#     inp1=int(input('Enter a number:'))

#     if inp1>0: 
#       print(inp1)
#       continue
# list1=[]
# for i in range(-5,5):
#     if i<=0:
#         continue
#     list1+=[i]
# print(list1)
# for i in list1:
#     print(i)



list3=[]
list2=['sun','mon','tue','wed','thurs','fri','sat']
for i in list2:
    # pass
    if i=='sun' or i=='sat':
        continue
    list3+=[i]
print(list3)


