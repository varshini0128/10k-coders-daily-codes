import keyword
print(keyword.kwlist)


firstname = "varshini"
surname = "siliveri"
 
firstname,surname = "varshini","siliveri"
print(surname)

a,b,c = 10,10,10

a=b=c = 10

apple = banana = "fruits"

print(banana)
 

a = 2585
b = 2585

print(a is b)  # True, both variables point to the same object in memory
print(a is not b)  # False, both variables point to the same object in memory
print(id(a))
print(id(b))

a = [1,2,3]
b=a
print(type(a)), print(type(b))
print(id(a)), print(id(b))
b.append(4)
print(a)