# num1 = int(input('enter  a number: '))
# num2 = int(input('enter  another number: '))
# # print(num1+num2)
# # print(num1-num2)
# # print(num1*num2)
# # print(num1/num2)
# # print(num1//num2)
# # print(num1%num2)
# # print(num1**num2)


# print(pow(num1,num2))
# print(divmod(num1,num2))
# print(abs(num1))
# print(abs(num2))
# print(round(3.5))


# # #Task : Pass a username and passsword using input function and validate them using if else statements
# # username = input("Enter your username: ")
# # password = input("Enter your password: ")
# # if username == "admin" and password == "admin123":
# #     print("Login successful!")
# # else:
# #     print("Invalid username or password.")


# #task pass a input to check whether you are student or employe if employee take course else complete your degree first
# role = input("Enter your role (student/employee): ").lower()
# if role == "employee":
#     print("You can take the course.")
# elif role == "student":
#     print("Please complete your degree first.")
# else:
#     print("Invalid role. Please enter 'student' or 'employee'.")

num1 = int(input("enter a number:"))
if num1%3==0 and num1%5==0:
    print('it is divisible by both 3 and 5')
elif num1%5==0:
    print('it is divisible by 5')

elif num1%3==0:
    print('it is divisible by 3')

var6=15
if type(var6) is int:
    print('it is of integer type')
else:
    print('it is not integer type')


str5 = "varshini siliveri"
if 'shini' in str5:
    print('y')
else:
    print('n')