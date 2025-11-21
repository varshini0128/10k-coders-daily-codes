h=()
j=tuple()
print(type(j))
#we can also declare it by 
j=1,2,3,4,5  #type is tuple because tuple is , seperated and store multiple values parenthesis are not mandatory
print(type(j))
k=9,     #it is still tuple 
k=9      #it is int
i=(10,12,11,14,13,15.910,10,10) #valid syntax 
# i=(10,20,30,40,50,,,,,,,,,,,)   #invalid syntax
print(i)

h=i.index(12)
print(h)
l=i.count(10)
print(l)
print(i[1:6])

l=10,20,3e1,30,'python'
print(l)  #ordered op: 10,20,3e1,30,'python'

# for x in 10 :  it gives error
# for x in 10,:  it gives 10 as output


f=1,2,34,568,7654,22332,3,32,11,2,1
p=sorted(f)
print(p,'******************************************')

#SET features
    # unordered
    # unidexed
    # mutable
    # duplicates are not allowed
    # heterogeneous 


# k={}      type is dictionary 

h=set()
print(type(h))

# set only allows immutable datatypes
# h={10,20,'python',2.3,4+4j,(1,2,3),[10,32,45]} #list is mutable so gets error 
h={10,20,'python',2.3,4+4j,(1,2,3)}
print(len(h))

h.add(200)
# print(h)
h.update({6,78,96,55,775,555})
print(h)

# merge -3types we can merge variable argument, iteration and uniono method 
k={1,2,3,4}
l={5,6,7,8,9}
res={*k,*l}  #variable length arguement
print(res)
for x in l:
    k.add(x)
print(k)


res1=k.union(l)         #union is  method of set
print(res1)

# to remove
k.remove(3)
print(k)

# without remove ---use pop 
l.pop() #randomly removes 
k.discard(2)    #it doesnot give error even if the value is not in the set

print(l)


#list lo and set lo values ni remove cheyali 

k1={10,20,30,40}
k2={10,50,30,20}
rs=k1.intersection(k2)
print(rs)
res3=k1&k2      #& is intersection
print(res3)

res5=k.symmetric_difference(k2)
print(res5)         #gives different values from both which dont match 
r=k1^k2       #  ^ is  symmetric difference


r1=k1.difference(k2)
r2=k1-k2        # - is difference
r3=k2-k1        # - is difference

a={1,2,3}
b={1,2,3,4,5}
res5=a.issubset(b)
res6=b.issuperset(a)
rees7=a.isdisjoint(b)
print(res5,res6,rees7)

