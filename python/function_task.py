# Function to calculate total bill
def total_bill(no_of_items, quantity, price, tax=5, discount=0, delivery_charge=0):
    subtotal = 0
  
    for i in range(no_of_items):
        subtotal += quantity[i] * price[i]
    
    tax_amount = (tax / 100) * subtotal
    subtotal += tax_amount
    
    discount_amount = (discount / 100) * subtotal
    subtotal -= discount_amount
    
    total = subtotal + delivery_charge
    
    return total


final_bill = total_bill(
    3,                  # no_of_items
    [2, 1, 3],          # quantities
    [150, 200, 50],     # prices
    tax=5, 
    discount=10, 
    delivery_charge=50
)
print("Total Bill: ", final_bill)



#write a variable length keyword arguements function to calculate total and percentage of a student in different subjects

def marks(**marks):
    total=0
    percentage=100
    for i in marks:
        total+=int(marks[i])
        percentage= (total / (len(marks)*100))*100
    print('total: ',total)
    print('percentage: ',percentage)
marks(maths='95',phys='84',eng='63',nlp='75',chem='94')


#Write a program to form a sentence out of words given at function calling to a variable length parameter.

def sentence_form(*words):
    sentence = ""  
    for word in words:
        sentence += word + " "  
    return sentence

sentence = sentence_form("My", "name", "is", "varshini", ",", "I", "am", "from", "hyd")
print("Formed Sentence:", sentence)



# #write functions to perform all arithmetic operations
def arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    modulus = a % b
    floor_division = a // b

    if b != 0:
       division = a / b
    else:
        'undefined'
    
    return addition, subtraction, multiplication, division, modulus, floor_division
add, sub, mul, div, mod, floor_div = arithmetic_operations(10, 5)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Modulus:", mod)
print("Division:", floor_div)

# #write a function to find factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
result = factorial(5)
print("Factorial:", result)

# #write a function to print 10 numbers in fibonacci series
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

fib_numbers = fibonacci_series(10)
print("Fibonacci Series:", fib_numbers)


# #check whether a number is perfect number using functions
def is_perfect_number(num):
    if num <= 0:
        return False
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num
number = int(input("Enter a number to check if it's a perfect number: "))
if is_perfect_number(number):
    print(number, 'is a perfect number.')
else:
    print(number, 'is not a perfect number.')


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
print('Prime numbers:',prime_list)