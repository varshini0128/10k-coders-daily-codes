import re

pattern = r"gr.y"

if re.match(pattern, "gray"):
    if re.match(pattern, "grey"):

            print('match found')





# caret nd dollar meta chatracyter

import re

pattern = r"^gr.y$"
if re.match(pattern,"grey"):
    print("match1")
    if re.match(pattern, "agrey"):
        print("match2")

    if re.match(pattern, "greym"):
        print("match3")

