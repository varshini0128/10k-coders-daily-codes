# Flatten a nested list (one level deep).
list1=[1,[2,3],4,5,[6,7,8],9,10]
temp=[]
for x in list1:
    if type(x)==list:
        for y in x:
            temp.append(y)
    else:
        temp.append(x)
print(temp)

# 2. Sort list of strings by length

lst = ["apple", "hi", "banana", "cat"]
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if len(lst[j]) > len(lst[j+1]):
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)

# 3. Common elements of two lists
a = [1,2,3,4]
b = [3,4,5]
u=[]
common_elements = []
for x in a:
    for y in b:
        if x == y:
            common_elements.append(x)
        
print(common_elements)

# 4. Elements only in first list
a = [1,2,3,4]
b = [3,4,5]
res = []

for x in a:
    found = False
    for y in b:
        if x == y:
            found = True
    if not found:
        res.append(x)

print(res)

# 5. Merge lists & remove duplicates
a = [1,2,3,4,6,3,4,2,4,4,22,2,34,3,2,3,2,3]
b = [3,4,5,43,43,4,3,4,3,43,43,4,3,4,3,4,3]
merged = []

for x in a:
    if x not in merged:
        merged.append(x)

for x in b:
    if x not in merged:
        merged.append(x)

print(merged)

# 6. Group list items into size 2
lst = [1,2,3,4,5]
groups = []

i = 0
while i < len(lst):
    groups.append([lst[i], lst[i+1]]) if i+1 < len(lst) else groups.append([lst[i]])
    i += 2
print(groups)

