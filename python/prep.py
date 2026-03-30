a=10
b=0o10
c=0X10
d=0B10
print(a)#10
print(b)#8
print(c)#16
print(d)#2




from sys import argv
sum=0
args=argv[1:]
for x in args :
    n=int(x)
    sum=sum+n
print("The Sum:",sum)


s='the python'
print(len(s))