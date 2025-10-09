try:
    a = 20
    b = 0
    print(a / b)
except ZeroDivisionError:
    print('there is a divide by zero error')

finally:
    print('this is going to execute no matter what')
