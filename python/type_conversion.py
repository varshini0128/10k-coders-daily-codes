# str to int
j='10'
print(type(j))
h=int(j)
print(type(h))
print(h+12)

# k='python' #we cant convert text string to integer


#int to str 

k=1010
print(k,type(k))
j=str(k)
print(j,type(j))


#int to float
j=10
print(float(j))


#bool to float
l=True
print(float(l))

#str to float
i='abc'
# print(float(i)) #error


# type_conversion
j=int(input('enter : '))   #we cant give text strings like'python we get error
print(j)
print(type(j))

h=bool(int(input('enter: ')))
print(h,type(h))

k1=list(map(int,input('enter:').split()))
print(k1)
print(type(k1))


h1=eval(input('enter: '))       #it takes what ever input and gives the correct type of data
print(h1)
print(type(h1))


#list to tuple,set
o=[1,2,3,4,5]
print(tuple(o))
print(set(o))


#list to dict
t=dict(('name','kumar'),('pin',101))
