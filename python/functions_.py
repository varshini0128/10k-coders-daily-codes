# def ==> keyword

# syntax:
# def function_name():

#to call a function syntax:
# function_name()

# line==>9
for x in range(10,20):
    if x%2==0:
        print(x)


#line==>15
for x in range(10,20):
    if x%2==0:
        print(x)


def even():
    for x in range(10,20):
      if x%2==0:
        print(x)
even()      #we can call this even function at any line 

h='python'
#create function to count length of string
def length():
    cou=0
    for x in h:
        cou+=1
    print(cou)

length()

def length1(p):  #paramaeter
    cou=0
    for x in p:
        cou+=1
    print(cou)

length1('ajay')   #arguement

# a1=10
# a2=20
def even1(a1,a2):
    for x in range(a1,a2):
        if x%2==0:
            print(x)
even1(30,40)

print() # it adds a line break in output

def check_num(h2):
    if h2>0:
        print('positive')
    elif h2<0:
        print('negative')
    else:
        print('zero')
check_num(23)

l1=10
l2=14
l3=13
# m=1
cou1=0
def prime(m):
    for x in range(2,m):        #1,2,5
        if m%x==0:
            cou1+=1
    if cou1==1:
        print('prime')
    else:
        print('not prime')
prime(11)
