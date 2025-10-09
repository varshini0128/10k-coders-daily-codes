import re


pattern = r"eggs"

if re.match(pattern,"baconeggseggseggsbacon"):
    print("match found")
else:
    print("no match found")



if re.search(pattern, "baconeggseggseggsbacon"):
    print('match found')
else:
    print('no match found')

if re.findall(pattern, "baconeggseggseggsbacon"):
    print('match found')
else:
    print('no match found')

print(re.findall(pattern, "baconeggseggseggsbacon"))




import re
string = "my name is varsh,hi i'm varsh"
pattern = r"varsh"
newstring = re.sub(pattern, "rob", string)
print(newstring)