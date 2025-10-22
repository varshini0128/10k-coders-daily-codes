##Multiplication Table (Nested Loops)

for i in range(1,11):
    for j in range(1,11):
        print(i,'x',j,'=',i*j)
    print()


# Right-Angled Triangle
n=5
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()


for i in range(n,0,-1):
    for j in range(1, i + 1):
        print(j,end=' ')
    print()

