#Ternary operator : It is a single line if else statement 
'''
it is called ternary because it takes 3 operands
1)condition
2)value when condition is true 
value when condition is false 
syntax : value condition value
A ternary operator must have an else statement after if unlike 
Ternary are used to evaluate simple conditions based on the output of the condition

'''

a=8
b=9
result='A is greater' if a>b else "B is greater"
print(result)

def category(age):
    return 'major' if age>18 else 'minor'
print(category(23))
print(category(17))

def even_odd(num):
    return 'even' if num%2==0 else 'odd'
print(even_odd(43))
print(even_odd(22))

#ternary with loops 
list1=[1,2,3,4,5,6,7,8,9,10]
evenOdd=['even' if n%2==0 else'odd' for n in list1]

# list2=['varsh','hema','ram','sita','geetha']
# strs=[]
# str1=['strs.append[i]' if len(list2[i]) > 5 else 'break' for i in list2]



# num=int(input("enter anumber:"))
# result='positive' if num>0 else 'Negative' if num<0 else 'zero'
# print(result)


# # write a program to pass a grade to a student based on his percentage using nested ternary operators 
# percentage=int(input('Enter percentage :'))
# grade='A' if percentage>90 else "B" if percentage>=80 else "c"
# print(grade)

def gm():
    return 'good morning'
def ga():
    return 'good afternoon'
def ge():
    return 'good evening'
def gn():
    return 'good night'
time = int(input('enter time in format of 24 hrs: '))
# greetings=gm() if time<12  12<= time <=15 ga()  ge() if time>15 else gn()

greetings = gm() if time < 12 else ga() and ga() if 12 <= time <= 15 else ge() and ge() if 15 <= time <= 20 else gn()


print(greetings)
