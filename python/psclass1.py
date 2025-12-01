k='python'
res=k[::-1]
print(res)
res1=''
for x in range(len(k)):
    # print(k[x])
    res1=k[x]+res1
print(res1)

start=0
end = len(k)-1
d=list(k)   # ['p' 'y' 't' 'h' 'o' 'n']
while start<end:
    d[start],d[end]=d[end],d[start]
    start+=1
    end-=1
print(d)
print(''.join(d))


temp=''
for x in range(len(k)-1,-1,-1):
    temp+=k[x]
print(temp)


print()
for x in range(1,10):
    print(x)
print()
for y in range(9,0):
    print(y)
print()
for z in range(9,-1,-2):
    print(z)


k='python'
tem2={}
for x in k:
    if x not in tem2:
        tem2[x]=1
    else:
        tem2[x]+=1
print(tem2)

temp3=''
for x in k:
    if x not in temp3:
        for y in k :
            cou=0
            if x ==y:
                cou+=1
        print(x,'==',cou,end=' ')
    temp+=x
    



