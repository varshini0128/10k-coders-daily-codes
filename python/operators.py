#Operators: operator is a symbol which is used to perform some operation on one or more than one operands and returns a result
# eg: a + b = c (an expression and a,b are operands +,= is operation c is result)
# operators: +,-,*,/,//,%,**

#Types of operators : 
# Arthimetic Operators:
                    #they are use to perform mathematical operations on two values  # operators: +,-,*,/,//,%,**
# a= 130
# b = 65

# # #addition
# print(a+b)

# #substraction
# print(a-b)

# #division
# print(a/b)      #prints quotient

# #floor division
# print(a//b)

# #modulus
# print(a%b)

# #exponent
# print(a**b)

# # Assignment Operators
#                     #they are used to perform assigning and operation along with assigning of variables/values
#                     # Operators: = ,  += , -= , /= , *= , %= , **=     
# var1 = 5
# var1 += 4  #augmented operations
# print(var1)  
# var1 -= 2
# print(var1)     
# var1 *= 2
# print(var1)
# var1 /= 2
# print(var1)
# var1 //= 2
# print(var1)
# var1 %= 2
# print(var1)

# # Comparison Operators
#                     #they are used to compare two values and returns a boolean value (True/False)
#                     # Operators: == , != , > , < , >= , <=

# # a = 10
# # b = 20
# # print(a == b)  #equal to
# # print(a != b)  #not equal to
# # print(a > b)   #greater than
# # print(a < b)   #less than       
# # print(a >= b)  #greater than or equal to
# # print(a <= b)  #less than or equal to   


# # val1 = 15
# # val2 = 'key'
# val1 = '1234'
# val2 = '123'
# print(val1 == val2)  # False, comparing int and str
# print(val1 != val2)  # True, they are not equal     
# print(val1 > val2)   # TypeError, cannot compare int and str
# print(val1 < val2)   # TypeError, cannot compare int and str            
# print(val1 >= val2)  # TypeError, cannot compare int and str
# print(val1 <= val2)  # TypeError, cannot compare int and str
# print(val1 == 15)  # True, comparing int with int



# # Logical Operators:    
#                     #they are used to combine conditional statements and returns a boolean value (True/False)
#                     # Operators: and , or , not     
#                     # or truth table:
#                     # a     b     a and b     a or b      not a      not b  
#                     # True  True   True        True        False      False
#                     # True  False  False       True        False      True  
#                     # False True   False       True        True       False
#                     # False False  False       False       True       True  
# # a = 10!=12
# # b= 5==5
# # print(a and b)  # True, both conditions are True
# # print(a or b)   # True, at least one condition is True
# # print(not a)    # False, negation of True is False
# # print(not b)    # False, negation of True is False

# # a = True
# # b = False

# # print(a and b)  # False, both conditions are not True
# # print(a or b)   # True, at least one condition is True  
# # print(not a)    # False, negation of True is False
# # print(not b)    # True, negation of False is True     

# # #Task:write a program to compare different data types which are supported by python and pass them to logical operators  
# # # eg: int, float, str, list, tuple, set, dict, bool 
# a = 10
# b = 10.0
# c = '10'
# d = [10]
# e = (10,0)
# f = {10}
# g = {10: 'ten'}
# h = True
# i = False

# print(a and b)  # True, both conditions are True    
# print(a or c)   # True, at least one condition is True
# print(not d)    # False, negation of True is False
# print(e and f)  # True, both conditions are True
# print(g or h)   # True, at least one condition is True
# print(not i)    # True, negation of False is True
# print(a and c)  # True, both conditions are True
# print(b or d)   # True, at least one condition is True
# print(not e)    # False, negation of True is False

# #falsy values: 0, 0.0, '', [], (), {}, set(), None, False
# #truthy values: any non-zero number, non-empty string, non-empty list, non-empty tuple, non-empty dict, non-empty set, True






# # Identity Operators:
#                     #they are used to compare the memory location of two objects and returns a boolean value (True/False)
#                     # Operators: is , is not
#                     # The "is" operator returns True if both variables point to the same object in memory
#                     # The "is not" operator returns True if both variables point to different objects in memory     
#                     #   eg: a is b , a is not b
#                     # Note: "==" operator compares the values of two variables, while "is" operator compares the memory locations of two variables
#                     # eg: a == b , a is b
         
# a = 10
# b = 10.0
# print(a==b)
# print(a is b)
# print(id(a))
# print(id(b))

# a = 10
# b = 10
# #id function returns the memory address of the object
# print(a is b)  # True, both variables point to the same object in memory
# print(a is not b)  # False, both variables point to the same object in memory
# print(id(a)) 
# print(id(b))
# c = [1,2,3]
# d = [1,2,3]
# print(c is d)  # False, both variables point to different objects in memory
# print(c is not d)  # True, both variables point to different objects in memory
# print(id(c))    
# print(id(d))

# # limit:-5 to 256 all integers are stored in the same memory location
# # beyond this range, new memory locations are created for each integer
# # this is done to optimize memory usage and improve performance

a = 257 
b = 257

print(a is b)  # True, both variables point to the same object in memory
print(a is not b)  # False, both variables point to the same object in memory
print(id(a))
print(id(b))


# import pickle

# a = pickle.loads(pickle.dumps(258))
# b = 258

# print(a is b)
# print(a is not b)
# print(id(a))
# print(id(b))

# c = int(a)  # converting str to int
# d = int(b)
# print(c is d)  # True, both variables point to the same object in memory
# print(c is not d)  # False, both variables point to the same object in memory
# print(id(c))
# print(id(d))    

# e = '256'
# f = '256'
# print(int(e) is int(f) ) # True, both variables point to the same object in memory
# print(int(e) is not int(f) ) # False, both variables point to the same object in memory
# print(id(int(e)))
# print(id(int(f)))

# # Membership Operators:
#                     #they are used to test if a sequence is presented in an object and returns a boolean value (True/False)
#                     # Operators: in , not in
#                     # The "in" operator returns True if the value is found in the sequence
#                     # The "not in" operator returns True if the value is not found in the sequence     
#                     #   eg: a in b , a not in b                                 
# list1 = ['varsh', 'kittu', 'jay', 'mini']
# print('varsh' in list1)  # True, 'varsh' is present in list1
# print('hello' in list1)  # False, 'hello' is not present in list1



amount = 5763
thousands = amount // 1000 # prints quotient
print("1000s:", thousands)

print(5763 % 1000)
print(36656 % 36000) #prints remainder


# # Bitwise Operators:
# Operators that perform operations on the binary representations of numbers, bit by bit. They manipulate the individual bits (0s and 1s) of a number.

# Common bitwise operators include:

# 1. & (Bitwise AND)
# 2. | (Bitwise OR)
# 3. ^ (Bitwise XOR)
# 4. ~ (Bitwise NOT)
# 5. << (Left Shift)
# 6. >> (Right Shift)
anni = 33
alex = 22
print(anni & alex)
print(alex | anni)
print(~alex)
print(alex>>2)
print(anni<<3)
print(anni^alex)
print(~5)