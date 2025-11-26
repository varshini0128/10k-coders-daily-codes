# h= tuple(x for x in range(1,10))
# # h= (x for x in range(1,10))     #generator generates values one by one
# print(h)
# print(h[3])
# print(next(h))
# print(next(h))

# for x in h:
#     print(x)

b=['data.csv','report.pdf','image.png']
res =[x.split('.')[1] for x in b] # x=data.csv
print(res)

for x in b:
    h=x.split('.')
    print(h)
    print(h[1])
 