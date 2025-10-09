def add(x):
    return x+2

newlist = [1, 2, 3, 4, 5]

result = list(map(add,newlist))

print(result)




newlist = [1, 2, 3, 4, 5]

result = list(map(lambda x: x+2,newlist))

print(result)
