k=[10,20,'python','java',3.3,22,43]
for x in k :
    if type(x)==int or float:
        print(x)
i=[10,20,30,40,50]
max1=0
for x in i:
    if x>max1:
        max1+=x
print(max1)
#min val
#second max
#list1=[ajay,101,124567890]
# choices=2 enter details check if any one match print all details
k=[11,12,13,14]
for x in range(len(k)):
    if k[x]%2==0:
        k[x]+=10
print(k)