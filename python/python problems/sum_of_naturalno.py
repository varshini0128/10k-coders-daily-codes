n = int(input("Enter a positive number: "))
total = 0

if n<=0:
    print('enter positive only')
else:
    for i in range(1, n + 1):
        total += i

print("Sum of first", n, "natural numbers is:", total)
