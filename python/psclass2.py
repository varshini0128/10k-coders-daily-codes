# k='duee'
# tem=''
# for x in k:
#     if x not in tem:
#         tem=tem+x
# print(tem)

# for x in range(10,20):
#     for y in range(2,x):
#         if x%y==0:
#             break
#     else: 
#          print(x)

# j='python'
# # for i in range(len(j)):
# #     if i%2==0:
# #         print(j[i])

# #prime index 
# for x in range(len(j)):
#     if x>1:
#         for y in range(2,x):
#             if x%y==0:
#                 break
#         else: 
#             print(j[x])
#     else:
#         print("not prime")

# # find largest word in sentence

# k='find largest word in sentence'
# r=''
# tem=0
# for x in j:
#     if len(x)>tem:
#         tem=len(x)
#         r=x
# print(tem)
# print(r)

n='find the first non repeating character'
for x in n:
    if n.count(x)==1:
        print(x)
        break
k=''
for x in n:
    if x not in k:
        cou=0
        for y in n:
            if x==y:
                cou+=1
        if cou==1:
            print(x)
            break
    k+=x


l='abc' #a b c ab bc ca 
p=[11,10,9,8,7,6] #ascending descending 
# check if a string contains only digits
p='abc123'
 











