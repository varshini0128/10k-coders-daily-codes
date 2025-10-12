list1=list(range(1,11,-1))
print(list1)
list2=list(range(11,1,-1))
print(list2)

str1='varsh'
print(len(str1))

tuple1=(1,2,3,45)
print(len(tuple1))
list3=['varsh','vamshi','kitu','sana','neha']
for i in range(len(list3)):
    print(list3[i])
print(list3[3])



#while loop: we use while loop when we dont know how many times a loop must iterate
#we pass a conditoon to while loop and the loop iterates as long as the condition is true.
#make sure that the condition given to the while loop is turned into false at some point.or else it will turn into infinite loop.

count=10
while count>=1:
    print(count)
    count-=1
print('loop completed')


list5=['varsh','vamshi','kitu','sana','neha']
count=0
length=len(list5)
while count<length:
    print(list5[count])
    count+=1
print('complete')

flag=True
i=10
while flag==True:
    print(i)
    i-=1
    if i==5:
        flag=False
print('loop exited at i==5')

#write a while loop to check whether the given credentials are matching or not

id_1='venkata'
pw1='venkata123'

while True:
    id=input('enter userid: ')
    pw=input('enter your password: ')

    if id==id_1 and pw ==pw1:
       print('login succesfully')
       break
    else:
        print('invalid credentials')




