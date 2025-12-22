# decorator.py
# decorator is a function that adds extra functionality to a function without changing its orginal code

def decorator(wish):
    def inner():
        print('hi')
        wish()
    return inner
    
@decorator
def wish():
    print('gm')

wish()

import time

def decorator(time_c):
    def inner():
        start_time=time.time()

        for x in range(10):
            # time.sleep(1)
            print(x)
        end_time=time.time()

        print("time:",end_time-start_time)
    return inner

@decorator
def time_c():
    for x in range(10):
        print(x)
time_c()

def authentication(main):
    def inner(k):
        if k == 'ajay':
            main(k)
        else:
            print('invalid')
    return inner

@authentication
def main(h):
    print("welcome to python",h)
main('ajay')
main('ravi')



def decorator(check_num):
    def inner(a):
        if a%2==0:
            print("even")
        else:
            print("odd")
    return inner

@decorator
def check_num(l):
    print(l)
check_num(11)





def prime(check_num):
    def inner(k):
        count1=0
        for i in range(1,k):
            if k%i==0:
                count1+=1
        if count1==1:
            print('prime')
        else:
            print('not prime')

    return inner


@prime
def check_num(l):
    print(l)

check_num(8)


def table1(t):
    def inner(k):
        if k%2==0:
            t(k)
        else:
            print('number is odd')
    return inner

@table1
def table(l):
    for x in range(1,11):
        print(l,'x',x,'=',l*x)
table(2)

print()
table(4)




