# #positive negative zero

# num = int(input('Enter a number:'))
# if num==0:
#     print('It is zero ')
# elif num>0:
#     print('It is a positive number')
# else:
#     print('It is a negative number')

# #even odd numbers

# val1=int(input('Enter a number'))
# if val1%2==0:
#     print('even number')
# else:
#     print('odd number')

# #greatest of three numbers
# num1=int(input('enter first number:'))
# num2=int(input('Enter second number:'))
# num3=int(input('Enter third number:'))

# if num1>num2 and num1>num3:
#     print(num1,'is greater')
# elif num2>num1 and num2 > num3:
#     print(num2,'is greater')
# elif num3>num1 and num3>num2:
#     print(num3,'is greater')

# #AGE category :
# age=int(input('Enter your age: '))
# if age<13:
#     print('child')
# elif age==13 or age<=19:
#     print('Teen')
# else:
#     print('Adult')


# #divisible by 5 and 11:
# int1=int(input('Enter a number'))
# if int1%5==0 and int1%11==0:
#     print('given number is divisble by both 5 and 11')
# else:
#     print('given number is not divisible by both 5 and 11')

# #leap year 

# year=int(input('Enter year:'))
# if year%4==0 and year%100!=0 or year%400==0:
#     print('it is a leap year')
# else:
#     print('It is not a leap year')


# #Pass or Fail 
# marks=int(input('Enter your marks out of 100: '))
# if marks>=40:
#     print('Pass')
# else:
#     print('Fail')

#vowel or consonant
char1=input('Enter a character: ')
if char1=='aeiou':
    print('vowel')
else:
    print('consonant')

#Login System

userid='admin'
pw1='1234'

while True:
    id=input('enter userid: ')
    pw=input('enter your password: ')

    if id==userid and pw ==pw1:
       print('login succesfully')
       break
    else:
        print('invalid credentials')

#Grade calculator
markss=int(input('Enter your marks: '))
if 90<=markss<=100:
    print('Grade A')
elif 80<=markss<=89:
    print('Grade B')
elif 70<=markss<=79:
    print('Grade C')
elif 60<=markss<=69:
    print('Grade D')
else:
    print('Grade F')

#square of numbers
for i in range(1,11):
    print(i**2)

#sum of digits :
 
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print("Sum of digits:", total)

