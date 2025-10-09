def factorial(x):
    if(x == 1):
        return 1
    else:
        return x*(factorial(x-1))

result = factorial(5)
print(result)

print(factorial(5))