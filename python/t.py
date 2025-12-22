s=[1,2,3,4]   #[1,3,6]
s1=[]
for x in s:
    x+=s1[-1] if s1 else 0
    s1.append(x)
print(s1)



