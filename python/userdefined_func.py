# #keyword arguements: These are used when we dont know in which order the parameters are in the function.

# # #area of rectangle using default parameters 
# # def area_of_rectangle(length=5,breadth=8):
    
# #     area= length * breadth
# #     perimeter = 2*(length+breadth)
# #     print('area: ',area)
# #     print('perimeter: ',perimeter)
   
# # area_of_rectangle()

# # def average_of_three(num1, num2, num3):
# #     avg = (num1 + num2 + num3) / 3
# #     print("Average:", avg)
# #     return avg


# # average_of_three(num2=10, num3=20, num1=30)

# # average_of_three(num1=10, num2=20, num3=30)



# # def add(*numbers):
# #     add_total=0
# #     for num in numbers:
# #         add_total+=num
# #         # print('multiplication: ',total)
# #     print(add_total)
# # add(7,5)
# # add(1,2,3,4,5,6,7,8)

# # def mul(*numbers):
# #     total=1
# #     for num in numbers:
# #         total*=num
# #         # print('multiplication: ',total)
# #     print(total)
# # mul(7,5)
# # mul(1,2,3,4,5,6,7,8)


# # def details(**values):
# #     for k in values:
# #         print(values[k])
# #     # for v in values.items():
# #     #     print(v)
    
# # details(name='jashwanth',age='22',add='hyderabad')


# # def details(**values):
   
# #     # print(values)
# #     return values
# # result = details(name='jashwanth', age='22', add='hyderabad')
# # print(result)

# # def details(**values):
   
# #     print(values)
# #     return values
# # details(name='jashwanth', age='22', add='hyderabad')


# #write a variable length keyword arguements function to calculate total and percentage of a student in different subjects

# def marks(**marks):
#     total=0
#     percentage=100
#     for i in marks:
#         total+=int(marks[i])
#         percentage= (total / (len(marks)*100))*100
#     print('total: ',total)
#     print('percentage: ',percentage)
# marks(maths='95',phys='84',eng='63',nlp='75',chem='94')


# #write functions to perform all arithmetic operations
# def arithmetic_operations(a, b):
#     addition = a + b
#     subtraction = a - b
#     multiplication = a * b
#     modulus = a % b
#     floor_division = a // b

#     if b != 0:
#        division = a / b
#     else:
#         'undefined'
    
#     return addition, subtraction, multiplication, division, modulus, floor_division
# add, sub, mul, div, mod, floor_div = arithmetic_operations(10, 5)
# print("Addition:", add)
# print("Subtraction:", sub)
# print("Multiplication:", mul)
# print("Modulus:", mod)
# print("Division:", floor_div)

# #write a function to find factorial of a number
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
# result = factorial(5)
# print("Factorial:", result)

# #write a function to print 10 numbers in fibonacci series
# def fibonacci_series(n):
#     fib_series = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_series.append(a)
#         a, b = b, a + b
#     return fib_series

# fib_numbers = fibonacci_series(10)
# print("Fibonacci Series:", fib_numbers)


# #check whether a number is perfect number using functions
# def is_perfect_number(num):
#     if num <= 0:
#         return False
#     sum_of_divisors = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum_of_divisors += i
#     return sum_of_divisors == num
# number = int(input("Enter a number to check if it's a perfect number: "))
# if is_perfect_number(number):
#     print(number, 'is a perfect number.')
# else:
#     print(number, 'is not a perfect number.')


#write a program to check prime or not
def is_prime(num1):
    if num1 <= 1:
        print(num1, 'is not a prime number.')
    for i in range(2, num1):
        if num1 % i == 0:
            print(num1, 'is not a prime number.')
        else:
            print(num1, 'is a prime number.')
            break
is_prime(0) 


#write a program to list out all prime numbers from 1 to 100
def prime_num():
    primes=[]
    for num in range(2,101):
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
    return primes
prime_list=prime_num()
print('Prime numbers from 1 to 100:',prime_list)
