k=[10,20,'python','java',3.3,22,43]
for x in k :
    if type(x)==int or float:
        print(x)
i=[10,20,30,40,50]
max1=0
for x in i:
    if x>max1:
        max1+=x
print(max1)
#min val
#second max
#list1=[ajay,101,124567890]
# choices=2 enter details check if any one match print all details
k=[11,12,13,14]
for x in range(len(k)):
    if k[x]%2==0:
        k[x]+=10
print(k)


# 1. Create a list of 5 numbers and print the first and last element.
lst = [10, 20, 30, 40, 50]

print("First:", lst[0])
print("Last:", lst[len(lst)-1])


# 2. Given a list, find the sum of all elements without using the sum() function.
lst = [1, 2, 3, 4, 5]

total = 0
for x in lst:
    total += x

print("Sum =", total)


# 3. Find the largest and smallest number in a list.
lst = [4, 9, 2, 7, 6]

largest = lst[0]
smallest = lst[0]

for x in lst:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x

print("Largest =", largest)
print("Smallest =", smallest)


# 4. Count how many times a specific element appears in a list.
lst = [1, 2, 3, 2, 4, 2]
target = 2

count = 0
for x in lst:
    if x == target:
        count += 1

print("Count =", count)


# 5. Reverse a list without using the reverse() function.
lst = [1, 2, 3, 4, 5]

rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Reversed list:", rev)


# 6. Check if a list is empty or not.
lst = []

if len(lst) == 0:
    print("List is empty")
else:
    print("List is not empty")


# 7. Given two lists, concatenate them into a single list without using +.
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

result = []

for x in lst1:
    result.append(x)

for x in lst2:
    result.append(x)

print("Concatenated list:", result)


# 8. Remove duplicates from a list and print the new list.
lst = [1, 2, 2, 3, 4, 4, 5]

unique = []

for x in lst:
    if x not in unique:
        unique.append(x)

print("List without duplicates:", unique)


# 9. Find the second largest number in a list.
lst = [10, 4, 8, 2, 15, 7]

largest = lst[0]
second = None

for x in lst:
    if x > largest:
        second = largest
        largest = x
    elif second is None or (x > second and x != largest):
        second = x

print("Second largest =", second)


# 10. Check if a particular element exists in a list.
lst = [3, 6, 9, 12]
target = 9

found = False

for x in lst:
    if x == target:
        found = True
        break

if found:
    print("Element exists")
else:
    print("Element does not exist")
