names = ["ram", "ravi", "sita"]
print(names)
print(names[1])


numbers = [1, 2, 3, 4]
print(numbers)
print(numbers[2])

abc = []
print(abc)

number = [1, 1, 1, 1, 1, 1, 1]
number[3] = 2
print(number)

newnumber = [2, 2, 2, 2, 2]
print(number + newnumber + numbers)

print(newnumber * 3)

fruits = ["mango", "apple", "banana", "peach"]
print("apple" in fruits)
print("orange" in fruits)
fruits.append('orange')
print(fruits)

print(len(fruits))

fruits.insert(1, "guava")
print(fruits)

print(fruits.index('orange'))


numbers = list(range(15))
print(numbers)

numbers = list(range(3, 10))
print(numbers)

numbers = list(range(3, 30, 6))
print(numbers)
