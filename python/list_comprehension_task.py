# 1. Numbers from 0 to 9
nums = [i for i in range(10)]

# 2. Squares of numbers 1 to 10
squares = [i*i for i in range(1, 11)]

# 3. Even numbers from 1 to 20
evens = [i for i in range(1, 21) if i % 2 == 0]

# 4. Extract characters from "python"
chars = [ch for ch in "python"]

# 5. Convert "python" to uppercase
upper = [ch.upper() for ch in "python"]

# 6. Multiples of 3 or 5 (1–20)
nums = [i for i in range(1, 21) if i % 3 == 0 or i % 5 == 0]

# 7. Squares of odd numbers (1–15)
squares = [i*i for i in range(1, 16) if i % 2 != 0]

# 8. Numbers ending with 5 (50–100)
nums = [i for i in range(50, 101) if i % 10 == 5]

# 9. Reverse each word
words = ["apple", "banana", "cherry"]
rev = [word[::-1] for word in words]

# 10. Remove zeros
nums = [10, 0, 20, 30, 0, 40]
res = [i for i in nums if i != 0]

# 11. Pairwise sums
sums = [x+y for x in [1,2,3] for y in [10,20,30]]

# 12. 3×3 matrix
matrix = [[j for j in range(3)] for i in range(3)]

# 13. Flatten list
flat = [x for sub in [[1,2,3],[4,5],[6]] for x in sub]

# 14. Square even, cube odd (1–10)
res = [i*i if i%2==0 else i*i*i for i in range(1,11)]

# 15. Multiplication table (1–3 × 1–3)
table = [[i*j for j in range(1,4)] for i in range(1,4)]

# 16. Extract vowels from "Python"
vowels = [ch for ch in "Python" if ch.lower() in "aeiou"]

# 17. ASCII values of "ABC"
ascii_vals = [ord(ch) for ch in "ABC"]

# 18. Uppercase A–Z
alphabets = [chr(i) for i in range(65, 91)]

# 19. Capitalize each word
text = "hello world python"
caps = [word.capitalize() for word in text.split()]

# 20. Even or Odd (1–10)
res = ["Even" if i%2==0 else "Odd" for i in range(1,11)]

# 21. Length of each word
lengths = [len(word) for word in ["Ajay","Python","Django"]]

# 22. Extract file extensions
ext = [file.split(".")[1] for file in ["data.csv","report.pdf","image.png"]]

# 23. Dictionary of squares (1–5)
squares = {i: i*i for i in range(1,6)}

# 24. Map characters to ASCII
ascii_map = {ch: ord(ch) for ch in "ABC"}

# 25. Combine two lists into dictionary
combined = {k:v for k,v in zip(['a','b','c'], [1,2,3])}

# 26. Prime numbers (1–100)
primes = [n for n in range(2,101) if all(n%i!=0 for i in range(2,n))]

# 27. Pairs where x ≠ y
pairs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

# 28. Palindrome numbers (1–100)
pal = [i for i in range(1,101) if str(i) == str(i)[::-1]]

# 29. Add elements from two lists
added = [a+b for a,b in zip([1,2,3], [10,20,30])]

# 30. Extract student names
students = [{'name':'Ajay','marks':80},{'name':'Riya','marks':90}]
names = [s['name'] for s in students]
