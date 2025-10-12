# #   even or odd

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")



# #  number is divisible by 5 but not by 10

# number = int(input("Enter a number: "))

# if number % 5 == 0 and number % 10 != 0:
#     print("divisible by 5 but not by 10")
# else:
#     print("Not valid")


# # find the biggest number among two

# A = int(input("Enter first number: "))
# B = int(input("Enter second number: "))

# if A > B:
#     print("Biggest is:", A)
# else:
#     print("Biggest is:", B)


# #  find the smallest number among two

# A = int(input("Enter first number: "))
# B = int(input("Enter second number: "))

# if A < B:
#     print("Smallest is:", A)
# else:
#     print("Smallest is:", B)


# #  number is divisible by 2, 3, and 6

# number = int(input("Enter a number: "))

# if number % 2 == 0 and number % 3 == 0 and number % 6 == 0:
#     print("number is divisible by 2, 3, and 6")
# else:
#     print("not satify given condition")


# #  person is eligible to vote

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


# #  student passed all subjects

# maths = int(input("Enter Maths marks: "))
# physics = int(input("Enter Physics marks: "))
# chemistry = int(input("Enter Chemistry marks: "))

# if maths >= 35 and physics >= 35 and chemistry >= 35:
#     print("Pass")
# else:
#     print("Fail")




# #  student passed in any one subject

# maths = int(input("Enter Maths marks: "))
# physics = int(input("Enter Physics marks: "))
# chemistry = int(input("Enter Chemistry marks: "))

# if maths >= 35 or physics >= 35 or chemistry >= 35:
#     print("Pass")
# else:
#     print("Fail")



# # student passed in any two subjects

# maths = int(input("Enter Maths marks: "))
# physics = int(input("Enter Physics marks: "))
# chemistry = int(input("Enter Chemistry marks: "))

# count = 0

# if maths >= 35:
#     count += 1
# if physics >= 35:
#     count += 1
# if chemistry >= 35:
#     count += 1

# if count >= 2:
#     print("Pass")
# else:
#     print("Fail")


# #  biggest number among three

# A = int(input("Enter first number: "))
# B = int(input("Enter second number: "))
# C = int(input("Enter third number: "))

# if A > B and A > C:
#     print("Biggest is:", A)
# elif B > C:
#     print("Biggest is:", B)
# else:
#     print("Biggest is:", C)


# #  smallest number among three

# A = int(input("Enter first number: "))
# B = int(input("Enter second number: "))
# C = int(input("Enter third number: "))

# if A < B and A < C:
#     print("Smallest is:", A)
# elif B < C:
#     print("Smallest is:", B)
# else:
#     print("Smallest is:", C)



#  number is a perfect square

import math

number = int(input("Enter a number: "))
sqrt_num = math.sqrt(number) 

if sqrt_num * sqrt_num == number:
    print("Perfect square")
else:
    print("Not a perfect square")
