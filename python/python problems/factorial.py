num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("❌ Factorial does not exist for negative numbers.")
elif num == 0:
    print("✅ The factorial of 0 is 1.")
else:
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f"✅ The factorial of {num} is {factorial}")




"""same easy method usinf for loop for factorial"""
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)
