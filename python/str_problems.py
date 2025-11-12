string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in string:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)


string = input("Enter a string: ")
result = ""

for ch in string:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)



string = input("Enter a string: ")

rev = ""      # make empty string for reverse
for ch in string:
    rev = ch + rev    # add each character in front

if string == rev:
    print("Palindrome")
else:
    print("Not Palindrome")



string = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in string:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print("String after replacing vowels:", result)



string = input("Enter a string: ")

checked = []  # to store already counted characters
for ch in string:
    if ch not in checked:
        count = 0
        for c in string:
            if ch == c:
                count += 1
        print(ch, ":", count)
        checked.append(ch)  # mark as counted



string = input("Enter a string: ")
upper = 0
lower = 0

for ch in string:
    # Check using ASCII values
    if 'A' <= ch <= 'Z':
        upper = upper + 1
    elif 'a' <= ch <= 'z':
        lower = lower + 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

