for i in range(1,4):
    if i>5:
        continue
    else:
        print(i)

items=['apple','banana','guava']
search='banana'
for i in items:
    if i==search:
        print('item found:',i)
        break