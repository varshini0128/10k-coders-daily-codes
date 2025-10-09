def square(x):
    return x**2

print(square(4))

result = (lambda x: x**2)(7)
print(result)

print((lambda x: x**2)(9))