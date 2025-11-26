#Create a dictionary where keys are 1,2,3… and values are cubes of keys
n = 5  
d1 = {i: i**3 for i in range(1, n+1)}
print(d1)


# Multiply all values in a dictionary
d3 = {'a': 2, 'b': 3, 'c': 4}
result = 1
for value in d3.values():
    result *= value
print(result)


#Sort a dictionary by keys
d4 = {"b": 2, "a": 1, "c": 3}
sorted_by_keys = dict(sorted(d4.items()))
print(sorted_by_keys)


# Keep only those items where values are divisible by 5
d5 = {'a': 10, 'b': 12, 'c': 25, 'd': 7}
filtered = {k: v for k, v in d5.items() if v % 5 == 0}
print(filtered)


# Find the smallest value in a dictionary
d6 = {'a': 10, 'b': 3, 'c': 6}
smallest = min(d6.values())
print(smallest)


#Find how many values are greater than 10 in a dictionary
d7 = {'a': 5, 'b': 12, 'c': 18, 'd': 7}
count = sum(1 for v in d7.values() if v > 10)
print(count)


d = {"a": 3, "b": 1, "c": 2}

sorted_values = sorted(d.values())
new_dict = {}

for val in sorted_values:
    for k, v in d.items():
        if v == val:
            new_dict[k] = v

print(new_dict)
