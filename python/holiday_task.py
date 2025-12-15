# 1. Reverse a string without slicing
s = "hello"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)


# 2. Check palindrome
s = "madam"
rev = ""
for ch in s:
    rev = ch + rev
print(s == rev)



# 3. Count vowels & consonants
s = "hello"
vowels = "aeiouAEIOU"
vc = cc = 0
for ch in s:
    if ch in vowels:
        vc += 1
    elif ch != " ":
        cc += 1
print(vc, cc)


# 4. Remove duplicates from string
s = "programming"
res = ""
for ch in s:
    if ch not in res:
        res += ch
print(res)



# 5. Most frequent character
s = "banana"
freq = {}
for ch in s:
    if ch not in freq:
        freq[ch] = 0
    freq[ch] += 1

max_char = ""
max_count = 0
for k in freq:
    if freq[k] > max_count:
        max_count = freq[k]
        max_char = k
print(max_char)




# 6. Convert sentence to title case manually
s = "hello world from python"
res = ""
make_cap = True
for ch in s:
    if make_cap and ch != " ":
        res += chr(ord(ch) - 32)
        make_cap = False
    else:
        res += ch
    if ch == " ":
        make_cap = True
print(res)





# 7. Check anagram
s1 = "listen"
s2 = "silent"

# count characters
count1 = {}
count2 = {}

for ch in s1:
    count1[ch] = count1.get(ch, 0) + 1
for ch in s2:
    count2[ch] = count2.get(ch, 0) + 1

print(count1 == count2)






# 8. Count words without split

s = "hi hello world"
count = 1
for ch in s:
    if ch == " ":
        count += 1
print(count)





# 9. Remove all spaces
s = "h e l l o"
res = ""
for ch in s:
    if ch != " ":
        res += ch
print(res)




# 10. Replace all occurrences
s = "hello"
res = ""
old = "l"
new = "x"
for ch in s:
    if ch == old:
        res += new
    else:
        res += ch
print(res)






# 11. First non-repeating character
s = "swiss"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break





# 12. Longest word in a sentence

s = "i love programming"
word = ""
longest = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

if len(word) > len(longest):
    longest = word

print(longest)







# 13. String contains only digits
s = "12345"
flag = True
for ch in s:
    if ch < "0" or ch > "9":
        flag = False
print(flag)




# 14. Reverse words in sentence
s = "hello world python"
word = ""
res = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        res = " " + word + res
        word = ""

res = word + res
print(res)





# 15. Implement atoi()
s = "1234"
num = 0
for ch in s:
    num = num * 10 + (ord(ch) - ord('0'))
print(num)


# 2. Numbers / Math (15 Questions)

# 16. Check if a number is prime
n = 17
prime = True

if n < 2:
    prime = False

for i in range(2, n):
    if n % i == 0:
        prime = False
        break

print(prime)

# 17. Find all prime numbers in a range
start = 1
end = 30

for num in range(start, end + 1):
    if num < 2:
        continue
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

# 18. Factorial (iterative & recursive)
# Iterative:
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# Recursive:
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
print(fact(5))

# 19. Fibonacci series (iterative & recursive)
# Iterative:
n = 10
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b

# Recursive:
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(7))


def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c

# function call
fibonacci(10)


# 20. Check if a number is Armstrong

# Example: 153 → 1³ + 5³ + 3³ = 153

n = 153
temp = n
sum = 0

while temp > 0:
    d = temp % 10
    sum += d*d*d
    temp //= 10

print(sum == n)

# 21. Find LCM of two numbers



# 22. Reverse number without converting to string
n = 1234
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n //= 10

print(rev)

# 23. Count digits in a number
n = 12345
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)

# 24. Sum of digits
n = 1234
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)

# 25. Check if a number is perfect

# Perfect number → sum of factors = number
# Example: 6 → 1+2+3=6

n = 6
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
print(s == n)

# 26. Sum of first n natural numbers
n = 10
s = 0
for i in range(1, n + 1):
    s += i
print(s)

# 27. Count trailing zeros in factorial

# (Counting multiples of 5)

n = 10
count = 0
i = 5
while i <= n:
    count += n // i
    i *= 5
print(count)

# 28. Check number palindrome
n = 121
temp = n
rev = 0

while temp > 0:
    d = temp % 10
    rev = rev * 10 + d
    temp //= 10

print(n == rev)

# 29. Check if number is Strong number

# Strong number → sum of factorial of digits = number
# Example: 145 → 1! + 4! + 5! = 145

def fact(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

n = 145
temp = n
s = 0

while temp > 0:
    d = temp % 10
    s += fact(d)
    temp //= 10

print(s == n)

# 30. Find nth Fibonacci term
n = 7
a, b = 0, 1

for i in range(n):
    a, b = b, a + b

print(a)


# 3. LISTS / ARRAYS (Q31–Q45)
# 31. Find max & min in a list without built-ins
arr = [3, 7, 2, 9, 5]

maxi = arr[0]
mini = arr[0]

for x in arr:
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x

print("Max =", maxi)
print("Min =", mini)

# 32. Remove duplicates from a list
arr = [1, 2, 2, 3, 4, 4]
res = []

for x in arr:
    if x not in res:
        res.append(x)

print(res)

# 33. Find second largest element
arr = [10, 20, 4, 45, 99]

max1 = max2 = -999999

for x in arr:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x

print(max2)

# 34. Rotate a list by n elements

# Example rotate left by n

arr = [1, 2, 3, 4, 5]
n = 2
res = []

for i in range(n, len(arr)):
    res.append(arr[i])
for i in range(0, n):
    res.append(arr[i])

print(res)

# 35. Merge two sorted lists
a = [1, 3, 5]
b = [2, 4, 6]

i = j = 0
res = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

while i < len(a):
    res.append(a[i])
    i += 1

while j < len(b):
    res.append(b[j])
    j += 1

print(res)

# 36. Find pairs with a given sum
arr = [1, 2, 3, 4, 5]
target = 6

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])

# 37. Subarray with maximum sum 
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = arr[0]
curr = 0

for x in arr:
    curr += x
    if curr > max_sum:
        max_sum = curr
    if curr < 0:
        curr = 0

print(max_sum)

# 38. Move all zeros to the end
arr = [0, 1, 0, 3, 12]
res = []

for x in arr:
    if x != 0:
        res.append(x)

zeros = []

for x in arr:
    if x == 0:
        zeros.append(x)

print(res + zeros)

# 39. Find missing number from list 1 to n

# Example list is missing one number

arr = [1, 2, 4, 5]
n = 5
total = 0

# sum 1..n manually
s = 0
for i in range(1, n + 1):
    s += i

for x in arr:
    total += x

print(s - total)

# 40. Check if list is palindrome
arr = [1, 2, 3, 2, 1]

i = 0
j = len(arr) - 1
flag = True

while i < j:
    if arr[i] != arr[j]:
        flag = False
        break
    i += 1
    j -= 1

print(flag)

# 41. Flatten a nested list
nested = [[1, 2], [3, 4]]
flat = []

for sub in nested:
    for x in sub:
        flat.append(x)

print(flat)

# 42. Find intersection of two lists
a = [1, 2, 3, 4]
b = [3, 4, 5]

res = []

for x in a:
    if x in b and x not in res:
        res.append(x)

print(res)

# 43. Find union of two lists
a = [1, 2, 3]
b = [3, 4, 5]
res = []

for x in a:
    if x not in res:
        res.append(x)

for x in b:
    if x not in res:
        res.append(x)

print(res)

# 44. Count frequency of each element
arr = [1, 2, 2, 3, 3, 3]
freq = {}

for x in arr:
    if x not in freq:
        freq[x] = 1
    else:
        freq[x] += 1

print(freq)

# 45. Sort a list without using sort()

# (Simple selection sort)

arr = [5, 2, 8, 1, 3]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)





# 4. DICTIONARIES / SETS (Q46–Q55)
# 46. Count frequency of elements using dictionary
arr = [1, 2, 2, 3, 3, 3]
freq = {}

for x in arr:
    if x not in freq:
        freq[x] = 1
    else:
        freq[x] += 1

print(freq)

# 47. Find common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5]

common = []
for x in a:
    for y in b:
        if x == y and x not in common:
            common.append(x)

print(common)

# 48. Merge two dictionaries (without using update)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = {}

for k in d1:
    merged[k] = d1[k]

for k in d2:
    merged[k] = d2[k]

print(merged)

# 49. Invert a dictionary (key ↔ value)
d = {"a": 1, "b": 2, "c": 3}
inv = {}

for k in d:
    val = d[k]
    inv[val] = k

print(inv)

# 50. Find unique elements in a list using set (manual implementation)
arr = [1, 2, 2, 3, 4, 4]
unique = []

for x in arr:
    if x not in unique:
        unique.append(x)

print(unique)

# 51. Remove duplicate values in dictionary
d = {"a": 1, "b": 2, "c": 1, "d": 3}
new = {}

for k in d:
    val = d[k]
    if val not in new.values():
        new[k] = val

print(new)

# 52. Check if two dictionaries are equal
d1 = {"a": 1, "b": 2}
d2 = {"a": 1, "b": 2}

equal = True
if len(d1) != len(d2):
    equal = False
else:
    for k in d1:
        if k not in d2 or d1[k] != d2[k]:
            equal = False

print(equal)

# 53. Sort dictionary by value (manual)
d = {"a": 3, "b": 1, "c": 2}

items = []
for k in d:
    items.append([k, d[k]])

# selection sort by value
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[j][1] < items[i][1]:
            items[i], items[j] = items[j], items[i]

sorted_dict = {}
for k, v in items:
    sorted_dict[k] = v

print(sorted_dict)

# 54. Create dictionary from two lists (manually)
keys = ["a", "b", "c"]
vals = [1, 2, 3]

d = {}
for i in range(len(keys)):
    d[keys[i]] = vals[i]

print(d)

# 55. Count number of keys with a certain value
d = {"a": 1, "b": 2, "c": 1, "d": 1}
value = 1
count = 0

for k in d:
    if d[k] == value:
        count += 1

print(count)



# 5. LOOPS / PATTERNS (Q56–Q65)
# 56. Print numbers 1–100
for i in range(1, 101):
    print(i)

# 57. Print even numbers 1–50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# 58. Print odd numbers 50–100
for i in range(50, 101):
    if i % 2 != 0:
        print(i)

# 59. Print square of numbers 1–10
for i in range(1, 11):
    print(i, "=", i*i)

# 60. Sum of first n natural numbers (loop)
n = 10
s = 0
for i in range(1, n+1):
    s += i
print(s)

# 61. Print multiplication table
n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# 62. Reverse a number using while loop
n = 1234
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n //= 10

print(rev)

# 63. Print triangle/star pattern
# *
# **
# ***
# ****
# *****

rows = 5
for i in range(1, rows+1):
    print("*" * i)

# 64. Print pyramid pattern of numbers
# 1
# 22
# 333
# 4444
# 5555

rows = 5
for i in range(1, rows + 1):
    print(str(i) * i)

# 65. Print diamond pattern using stars
#   *
#  ***
# *****
#  ***
#   *

n = 3

# upper part
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))

# lower part
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))




# 7. OOP / CLASSES (Q66–Q75)
# 66. BankAccount class (deposit, withdraw, check balance)
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)

# Example
acc = BankAccount(500)
acc.deposit(200)
acc.withdraw(100)
acc.check_balance()

# 67. Rectangle class (area & perimeter)
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)

r = Rectangle(5, 3)
print(r.area())
print(r.perimeter())

# 68. Circle class (area & circumference)
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def circumference(self):
        return 2 * 3.14 * self.r

c = Circle(4)
print(c.area())
print(c.circumference())

# 69. Inheritance: Person → Employee
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

e = Employee("John", 50000)
print(e.name, e.salary)

# 70. Implement class method & static method
class Demo:
    x = 10

    @classmethod
    def show_x(cls):
        print(cls.x)

    @staticmethod
    def greet():
        print("Hello!")

Demo.show_x()
Demo.greet()

# 71. Encapsulation (private attributes & getters/setters)
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, m):
        if m >= 0:
            self.__marks = m

s = Student("Alice", 85)
s.set_marks(90)
print(s.get_marks())

# 72. Polymorphism (method overriding)
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()

# 73. Operator overloading (add two objects)
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

a = Number(10)
b = Number(20)
c = a + b
print(c.value)

# 74. Simple calculator using class methods
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

cal = Calculator()
print(cal.add(10, 5))
print(cal.mul(3, 4))