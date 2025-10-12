# num = int(input('Enter a number:'))
# if num==0:
#     print('It is zero ')
# elif num>0:
#     print('It is a positive number')
# else:
#     print('It is a negative number')



# num1=int(input('enter first number:'))
# num2=int(input('Enter second number:'))
# num3=int(input('Enter third number:'))

# if num1>num2 and num1>num3:
#     print(num1,'is greater')
# elif num2>num1 and num2 > num3:
#     print(num2,'is greater')
# else:
#     print(num3,'is greater')



# year=int(input('Enter year:'))
# if year%4==0 and year%100!=0 or year%400==0:
#     print('it is a leap year')
# else:
#     print('It is not a leap year')



# side1= int(input('Enter side1:'))
# side2= int(input('Enter side2: '))
# side3=int(input('Enter side3: '))
# if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
#     print('Using given sides we can form a triangle')
# else:
#     print('We cant form a triangle with the given sides')

# list1=[]
# for i in range(1,26):
#     if i%2==0:
#         # print(i)
#         list1+=[i]
# print(list1)

# for i in range(1,11):
#     print('35 x ',i,'=', 35*i)

# sum_total=0
# product_total=1  #factorial
# for i in range(1,11):
#     sum_total+=i
#     product_total*=i
# print(sum_total,product_total)


num2=int(input('enter a number:'))
while num2>0:
    digit=num2%10  
    print(digit)
    num2//=10

# num2=int(input('enter a number:'))
# list2=[]
# while num2>0:
#     digit=num2%10  
#     list2.append(digit)
#     num2//=10
# print(list2)

num2 = int(input("Enter a number: "))
digits = []

# Extract digits
while num2 > 0:
    digit = num2 % 10
    digits.append(digit)
    num2 //= 10

for d in reversed(digits):
    print(d)




 


