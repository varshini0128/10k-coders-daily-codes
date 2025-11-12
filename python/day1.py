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
 
c=3e1 #printing float num without '.'  so we use 'e' and e=10**1/2/3/5/4...........
c1=3E1 #we can use 'e' and 'E' 
print(c1)
print(c)
print(type(c))


k=True
k1=False
res=k1+k1  #0  #when asks for prove that True value is 1 and false value is 0
res2=k+k   #2
print(res2)
print(res)




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

