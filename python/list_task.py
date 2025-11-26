# 1. Create a list of 5 numbers and print the first and last element.
l1=[1,2,3,4,5]
print(l1[0],l1[4])

# 2. Given a list, find the sum of all elements without using the sum() function.
l2=[10,20,30,40,50]
sum1=0
for x in l2:
        sum1+=x
print(sum1)

# 3. Find the largest and smallest number in a list.

l3=[1,2,3,4,5]
smallest=10
greatest=0
for x in l3:
    if x>greatest:
          greatest=x
    elif x<smallest:
          smallest=x
print('smallest: ', smallest)
print('greatest: ',greatest)

# 4. Count how many times a specific element appears in a list.

l4=[1,2,3,4,5,6,7,8,9,10,2,4,6,8,11,53]
k=()
for x in l4:
      print(x,":", l4.count(x))
print(k)

# 5. Reverse a list without using the reverse() function.
l5=[1,2,3,4,5,6,7,8,9,10]
reversed_list = l5[::-1]
print(reversed_list)

# 6. Check if a list is empty or not.
l6=[1,2,3]
if l6==[]:
      print('empty')
else:
      print('not empty')
    
# 7. Given two lists, concatenate them into a single list without using +.
l6=[1,2,3]
l7=[4,5,6]
for x in l7:
    l6.append(x)
print(l6)

# 8. Remove duplicates from a list and print the new list.
l8=[1,2,3,1,2,3]
new_list=[]
for x in l8:
      if x not in new_list:
            new_list.append(x)
print(new_list)

# 9. Find the second largest number in a list.
l9=[20,10,40,30,60,50,40]
sorted_list=[]
l9.sort
print(l9[-2])

# 10. Check if a particular element exists in a list.

l10=[1,2,3,4,5,6,7]
k=int(input('enter a number: '))
if k in l10:
      print('exist')
else:
      print('not exist')
      
