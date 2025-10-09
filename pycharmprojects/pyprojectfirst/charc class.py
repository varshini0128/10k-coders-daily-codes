import re
#aa2
pattern = r"[a-z][a-z][0-9]"
if re.search(pattern,"ah9"):
    print("match found")


#star  and meta character


import re

pattern = r"eggs(bacon)*"

if re.match(pattern, "eggs"):
   print("match found")
   if re.match(pattern, "eggsbacon"):
       print("match founded")

       if re.match(pattern, "baconeggsbacon"): #it wont execute 
           print("match found")


#GROUP

import re

pattern = r"bread(eggs)*bread"

if re.match(pattern,"breadeggseggseggsbread"):
    print("matched")
