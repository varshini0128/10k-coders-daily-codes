# d={'name':'ajay','pin':101}
# print(type(d))
# d.update({'age':16})
# print(d)
# d.pop('pin')
# print(d)

d1={'ajay':{'office':123456789,'home':987654321}}
print(d1['ajay'])
print(d1['ajay']['office'])
print(d1['ajay']['home'])

d2={'[1,2,3]':'python'}
print(d2) #gets output but  if d2={[1,2,3]:'python'} no op or  error  we cnat keep mutabale data types as keys but we can give
#mutable types as keys 
d4={'ajay':[1,2,34,4,5]}

d5={'name':'ajay'}
d5['mobile']=123456789      #without using update 
print(d5)

school= [
        {'name':'ajay','pin':101,'age':15},
        {'name':'sai','pin':101,'age':15},
        {'name':'ram','pin':101,'age':15},
        {'name':'ravi','pin':101,'age':15},
        {'name':'kavya','pin':101,'age':15},
        {'name':'hema','pin':101,'age':15},
        {'name':'ajith','pin':101,'age':15},
        {'name':'arun','pin':101,'age':15}
]
print(school[4])
n=eval(input('enter in or student details: '))
for x in school:
    if x['pin']==n or x['name']==n:
        print(x)
        for a,b in x.items():
            print(a,'===',b)



l={'name':'ram','age':23}
for x,y in l.items():
    print(x,'-->',y)



i=[]
n=int(input('enter no of students: '))
for x in range(n):
    d={}
    d['name']=input('enter student name: ')
    d['pin']=int(input('enter student pin: '))
    d['age']=int(input('enter student age: '))
    i.append(d)

print(l)

j={'a':10,'b':20,'c':30}
j.popitem()     #to remove last element in dictionary
# j.popitem('b')    error
print(j) 
j.pop('b')
# j.pop()     error

'keys   values     items'
o={'a':10,'b':20}
tem={}
for a,b in o.items():
   tem[b]=a
print(tem)

