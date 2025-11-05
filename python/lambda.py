#Lambda : Lambda functions are simple and anonymous(nameless) function to write non reusable codes 
#Syntax: lambda parameters : expression
#it does not need a return statement ,lamda functions return automatically
# lambda are used only for small and simple it is not suitable for complex operations 

def add_func(a,b):
    return a+b
add_func(11,3)

add_num=lambda a,b:a+b
print(add_num(3,4))

square=lambda a:a**2
print(square(5))

#F = C * 9/5 +32
#C = F-32 * 5/9

celToFar=lambda c: c * (9/5) +32
print(celToFar(37))

FarToCel = lambda f : (f-32) * (5/9)
print(FarToCel(98))


evenOdd = lambda a: "Even" if a%2==0 else "Odd"     #Ternary Operators
print(evenOdd(3))

greatest=lambda a,b:"a is greater" if a>b else "b is greater"
print(greatest(50,54))


#Lambda function with sort
names=['ram','ravi','tej','anuhya','sita']
names.sort(key=lambda name:len(name))
print(names)

nums=[123,3456,7899,2775,678,2345,567887]
nums.sort(key=lambda num:num)
print(nums)

#lambda with map(): It is used to apply a function over a data/sequence of data 
#Syntax: map(function,sequence)

list1=[1,2,3,4,5]
square_list=list(map(lambda num: num**2,list1))
print(square_list)

#lambdawith filter(): It is used 
list2=[1,2,3,4,5,6,7,8,9,10]
even_filter=list(filter(lambda num: num%2==0,list2))
print(even_filter)


#lambda with reduce(): 
from functools import reduce
list3=[1,2,3,4,5,6]
reduce_val=reduce(lambda num1,num2: num1+num2,list1)
print(reduce_val)

namess=['Ajith Kumar','Viswa Teja','Naga Swarop','Samuel Paul','Vishnu Varshan']
# op:[AK,VT,NS,SP,VV]
