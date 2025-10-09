# Data type : categorizing a value into a certain type 
# primitive : int, float, string, boolean, none , complex
# non primitive : list, tuple, set, frozen set, and dictionary 

# primitive are immutable 
# integer type  
var2 = 2e3 # we defined a variable with a integer daata type 
print(var2)

#float 
float1 = 3.3
print(type(float1))

#string example
str4 = 'varsh'
str5 = '22'
str6 = '7.0'
print(type(str4),type(str5),type(str6), str4.upper(), str5.lower()) #upper() & lower()  are used to convert a string to upper case and lower case


#boolean example TRUE and FALSE
print(1>5)
print(8>5)
varsh = 'hey varsh'
print(varsh == "world")



#Complex numbers: it is a combination of a real and imaginary number along with a constant
# ex: a+bj where j = sqrt(-1)
#we use complex numbers in polynomial functions and signal processing


comp1 = 2+3j
comp2 = 5+10j
print(comp1) #printing complex number
print(type(comp1))  #type of data
print(comp1.real)  #to get the real part of my complex number
print(comp1.imag)   #to get the imaginary part of my complex number

#in addition and substraction the operation is performed on real part and imaginary part seperately
print(comp1 + comp2)
print(comp1 - comp2)

# com1=a+bj
# com2=c+dj
# com1*com2 = (ac-bd)+(ad+bc)j
# com1/com2 =(ac+bd)+(bc-ad)jc**2+d**2

print(comp1*comp2)
print(comp1/comp2)

# magnitude = sqrt(a**2+b**2)      distance of a number from orgin in a plane
print(abs(comp1))  #absolute function is used to find magnitude of a number
print(abs(comp2)) #answer?? 



#none type example
none1 = None
print(type(none1))
print(None)


var3=10 
var3+10
print(var3)

#type() is used to know the type of a data
print(type(5))
print(type(None))

# Task1 : Demonstrate primitive datatype 
num1 = 2 
float2= 2.2
string = "varsh"
boolvalue = 2<5
nonevalue = None 
print(num1, float2, string, boolvalue, nonevalue)
print(type(num1))
print(type(float1))
print(type(string))
print(type(boolvalue))
print(type(nonevalue))

# #non primitive datatypes Non primitive types are immutable except frozen set and tuple


#list : It is used to store sequence of data using square brackets  list is mutable 
#We can store data of multiple datatypes  in a list

list1= [1,3.3,"string", True, None, 3+6j]
print(list1)
# to add a value to an existing list, i use append()
# list1.append("varsh")
# print(list1)

#indexing : it is used to access / modify individual values in a sequence 
print(list1[0])
list1[2] = "varsh"
list1[1] = 7.0
print(list1)
# negative indexing : this is used to access individual values from back 
list1[-2] = False
print(list1)
print(len(list1))  #len(): returns no of values in a sequence
print(list1.count(3.3)) #count(): used to get the number of time a value is repeated
print(list1.count("varsh")) #count(): used to get the number of time a


 #tuples: in tuple we can provide data types and list also access the values using indexing .
 #  it looks similar to list but instead of square of braces we use open braces()
 # tupleName=(value1,value2,value3,,,,,,,)
 #tuples are immutable 
#since tuple is immutable we cant perform append or other actions

tuple = (22, 7.0, "varsh", None, 'sri indu', 123456543, [1,2,3,4,5], (6,7,8))
print(tuple) 
print(len(tuple))  #len(): returns no of values in a sequence 
print(tuple.count('varsh')) #count(): used to get the number of time a value is repeated 
print(tuple.count('vamshi')) #returns 0 if values are not in tuple or sequence
print(tuple[-1][2]) #double indexing 
print(tuple[-2][4])
# tuple[1] = 8.0 #gives error as tuple is immutable

#Task: Create a list with your name , college, cgpa, and later add your address to it using append 

mydatalist = ["varshini", "Sri Indu", 7.0]
print(mydatalist)
mydatalist.append("Dilsukhnagar")
print(mydatalist) 
print(mydatalist.count(7.0))  #count(): used to get the number of time a value is repeated
print(len(mydatalist))  #len(): returns no of values in a sequence
print(mydatalist[0])  #indexing to access individual values in a sequence
print(mydatalist[-1]) #negative indexing to access individual values from back in a sequence

#set: set is used to store unique and unordered elements
# set is mutable we can add, remove elements from it 

set1 = {1,2,3,1,2,3,'hema','rahul','satya'}
print(set1)
# print(set1[0]) gets error cant use indexing in set because it is unordered

set1.add(5)
print(set1) # it adds value 5 randomly we cant define which place to add 5 
set1.remove(3)
print(set1)
froset=frozenset([1,2,3,4,5,1,2,3,4,5])
print(froset)

# froset.add(9) gives error

#dictionary: it is used to store data in the form of key-value pairs 
# we can access values in dictionary using keys
#all the keys of my dictionary of to be immutable data type
#we can access only keys of a dictionary using .keys()  function
#we can access only values of a dictionary using .values()  function
#we can access both keys and values of a dictionary using .items()  function

dict1 = {'name':'varsh', 'age': 22,'college': 'siiet','cgpa':7.0,'mobile no': 12345678}
print(dict1['age'])
print(dict1['cgpa'])# we get values as output 
print(dict1.keys())
print(dict1.values())
print(dict1.items)

dict2= {1:'varsh', 2:'sanjana', 3: 'varsha'}

print(dict2)

# dict3 = {[1,2,3]:'list',(1,2,3,4):'tuple',{1,2,34,22}: 'set'} we get errors because list and set are mutable and 
# all the keys of my dictionary of to be immutable data type

var2 = 2e3
print(var2)


#type conversion : python automatically converts a type of a value during execution
int3 = 4
float3 = 2.3
print(int3+float3)

#type casting : here we manually change the type of a datatype
#in short it is done by the programmers instead of compiler

print(int(int3+float3))

#creating a complex number using type casting
a=3
b=5
print(complex(a,b))


bool2 = True #note in python true value is considered as 1 and  false as 0
int4 = 4
print(bool2+int4)

str1 ="varshini"
print(list(str1))
print(set(str1))


