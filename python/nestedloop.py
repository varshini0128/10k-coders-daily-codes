#nested loops :
#writing a loop inside another loop
#for inside a for
#while inside a while
#for inside a while
#while inside a for 
#for every one iteration of outer loop,innerloop completes all its iteration
for i in range(5):
    for j in range(5):
        print(i,j)


#In patterns the outer loop decides the number of rows 
# where as the inner looop decides th enumber of columns

for i in range(5):
    while j==4:
        print("*" ,end='')
        break
    print()

for i in range(6):
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# while True:
#     for i in range(5):
#         print('*',end=' ')
#         False
        
# print()
