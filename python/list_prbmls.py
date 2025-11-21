
# #list : It is used to store sequence of data using square brackets  list is mutable 
# #We can store data of multiple datatypes  in a list
#features:
        #ordered                     same order when we print
        #mutable                     can be changed
        #allow duplicates            
        #hetergenous object          different datatypes can be stored
        #supports nested lists
        #builtin methods'iterable
        #indexable and slicable

list1= [1,3.3,"string", True, None, 3+6j]
print(list1)

#LIST METHODS
    #APPEND
            # to add a value to an existing list, we use append()
            # list1.append("varsh")
            # print(list1)
    #REMOVE
            # it is used to remove specific element from list 
            # list1.remove(1)
    #POP
            #it is used to remove last value or particular indexed value in a list
            #list1.pop()
            # list1.pop(1) here 1 is index 
            # list1.pop(21) #indexerror
            # h=list1.pop(2) to show or display the popped value
    #INSERT
            #it is used to insert a value at a certain index 
            # list1.insert(1,200)       first we need to pass index position and then value in  inside method
    #EXTEND
            #it is used to add more than one values at a time then we use extend
            #list1.extend(10,22,33)
        #merge:     a=[12,23,3,4,5,6,4]
                    # b=[1234,2345345,78765345,765]
                    # merge=a+b
        #repeat:    # repeat=a*2


# #indexing : it is used to access / modify individual values in a sequence 
# print(list1[0])
# list1[2] = "varsh"
# list1[1] = 7.0
# print(list1)
# # negative indexing : this is used to access individual values from back 
# list1[-2] = False
# print(list1)
# print(len(list1))  #len(): returns no of values in a sequence
# print(list1.count(3.3)) #count(): used to get the number of time a value is repeated
# print(list1.count("varsh")) #count(): used to get the number of time a value is repeated

h=[1,2,3,4]
h+=[9]      #without append
print(h)
print("****************************************************************************")

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

#update the odd index values by multipying them with 2
k=[10,11,12,13,14,15,16,17]
for x in range(len(k)):
    if x % 2==1:
        k[x]=k[x]*2
print(k)   #op: [10, 22, 12, 26, 14, 30, 16, 34]

#to find factors of a number:
a=12
for x in range(1,12):
    if a%x==0:
        i=print(x)



#check prime or not 
b=5
count=0
for x in range(1,b+1):
    if a%x==0:
        count+=1
if count==2:
    print('prime')
else:
    print("not prime")


h=[10,11,12,13,14,15,16,17]
for x in h:
    cou=0
    for y in range(1,x):
        if x%y==0:
            cou+=1
    if cou==1:
        print("prime",x)
        x*=2
        print(x)
    else:
        print("not prime")

s=[]

















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
