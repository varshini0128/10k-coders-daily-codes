#1 to 10 :
for i in range(1,11):
    print(i)

#sum of first 10 numbers
sum_total=0
for i in range(1,10):
    sum_total+=i
print(sum_total)


#Multiplication table
num1=int(input('Enter a number for multiplication table: '))
for i in range(1,11):
    print(num1,' x ',i,'=', num1*i)

#Even Numbers
for i in range(1,51):
    if i%2==0:
        print(i)

#Factorial Number:

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is", fact)

#sum of even numbers
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)


# Reverse Counting: Print numbers from 10 down to 1
for i in range(10, 0, -1):
    print(i)

str1=input('Enter a string: ')
count=0
for i in str1:
    if i in 'aeiou':
        count+=1
print('vowels count:', count)
