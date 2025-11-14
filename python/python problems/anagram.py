str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


from collections import Counter
a='listen'
b='silent'
if Counter(a)==Counter(b):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


h='mile'
j='lime'
i={}
k={}
for x in h:
    if x not in i:
        i[x]=1
    else:
        i[x]+=1

for x in j:
    if x not in k:
        k[x]=1
    else:
        k[x]+=1
if i==k:
    print('anagrams')
else:
    print('not anagrams')