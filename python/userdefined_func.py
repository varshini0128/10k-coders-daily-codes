#keyword arguements: These are used when we dont know in which order the parameters are in the function.

# #area of rectangle using default parameters 
# def area_of_rectangle(length=5,breadth=8):
    
#     area= length * breadth
#     perimeter = 2*(length+breadth)
#     print('area: ',area)
#     print('perimeter: ',perimeter)
   
# area_of_rectangle()

# def average_of_three(num1, num2, num3):
#     avg = (num1 + num2 + num3) / 3
#     print("Average:", avg)
#     return avg


# average_of_three(num2=10, num3=20, num1=30)

# average_of_three(num1=10, num2=20, num3=30)



# def add(*numbers):
#     add_total=0
#     for num in numbers:
#         add_total+=num
#         # print('multiplication: ',total)
#     print(add_total)
# add(7,5)
# add(1,2,3,4,5,6,7,8)

# def mul(*numbers):
#     total=1
#     for num in numbers:
#         total*=num
#         # print('multiplication: ',total)
#     print(total)
# mul(7,5)
# mul(1,2,3,4,5,6,7,8)


# def details(**values):
#     for k in values:
#         print(values[k])
#     # for v in values.items():
#     #     print(v)
    
# details(name='jashwanth',age='22',add='hyderabad')


# def details(**values):
   
#     # print(values)
#     return values
# result = details(name='jashwanth', age='22', add='hyderabad')
# print(result)

# def details(**values):
   
#     print(values)
#     return values
# details(name='jashwanth', age='22', add='hyderabad')


#write a variable length keyword arguements function to calculate total and percentage of a student in different subjects

def marks(**marks):
    total=0
    percentage=100
    for i in marks:
        total+=int(marks[i])
        percentage= (total / (len(marks)*100))*100
    print('total: ',total)
    print('percentage: ',percentage)
marks(maths='95',phys='84',eng='63',nlp='75',chem='94')


#write a program to form a sentence out of words given at function calling to a variable length parameters