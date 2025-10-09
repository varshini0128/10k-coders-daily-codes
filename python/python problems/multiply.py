for i in range(1, 2):        # Outer loop → table number
    for j in range(1, 11):    # Inner loop → multiply with 1 to 10
        print(f"{i} x {j} = {i*j}")
    print()  # Blank line after each table


s = input("Enter a sentence: ")
words = s.split()
print("Word count:", len(words))

s = input("Enter a string: ")
print("Lowercase:", s.lower())

s = input("Enter a string: ")
print("Lowercase:", s.upper())

lst = ["apple", "banana", "cherry"]
upper_lst = [x.upper() for x in lst]
print(upper_lst)

s = input("Enter string: ")
print(s == s[::-1])
