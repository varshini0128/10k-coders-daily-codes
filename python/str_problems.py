# # string = input("Enter a string: ")
# # vowels = "aeiouAEIOU"
# # count = 0

# # for ch in string:
# #     if ch in vowels:
# #         count += 1

# # print("Number of vowels:", count)


# # string = input("Enter a string: ")
# # result = ""

# # for ch in string:
# #     if ch not in result:
# #         result += ch

# # print("String after removing duplicates:", result)



# # string = input("Enter a string: ")

# # rev = ""      
# # for ch in string:
# #     rev = ch + rev    

# # if string == rev:
# #     print("Palindrome")
# # else:
# #     print("Not Palindrome")



# # string = input("Enter a string: ")
# # vowels = "aeiouAEIOU"
# # result = ""

# # for ch in string:
# #     if ch in vowels:
# #         result += "*"
# #     else:
# #         result += ch

# # print("String after replacing vowels:", result)



# string = input("Enter a string: ")

# checked = []  
# for ch in string:
#     if ch not in checked:
#         count = 0
#         for c in string:
#             if ch == c:
#                 count += 1
#         print(ch, ":", count)
#         checked.append(ch)  



# # string = input("Enter a string: ")
# # upper = 0
# # lower = 0

# # for ch in string:
# #     # Check using ASCII values
# #     if 'A' <= ch <= 'Z':
# #         upper = upper + 1
# #     elif 'a' <= ch <= 'z':
# #         lower = lower + 1

# # print("Uppercase letters:", upper)
# # print("Lowercase letters:", lower)


# # h='ajay@!#$%^&123456789'



# # # 1. Reverse a string
# # # Example: Input: "hello" → Output: "olleh"
# # str1=input('enter a string: ')
# # temp=''
# # for x in str1:
# #     temp=x+temp
# # print(temp)

# # # 2. Check if a string is a palindrome
# # # Example: "madam" → True
# # str1=input('enter a string: ')
# # temp=''
# # for x in str1:
# #     temp=x+temp
# # if temp==str1:
# #     print('palindrome')
# # else:
# #     print('not a palindrome')
# # print(temp)


# # # 3. Count vowels and consonants in a string

# str2=input('enter string ')
# v_count=0
# c_count=0
# for x in str2:
#     if x in 'aeiouAEIOU':
#         v_count+=1
#     else:
#         c_count+=1
# print('vowels count is ', v_count)
# print('consonants count is ', c_count)

# # 4. Find the frequency of each character in a string
# str3=input('enter a string ')
# h=[]
# for x in str3:
#     if x not in h:
#         count=0
#         for c in str3:
#             if x==c:
#                 count+=1
#         print(x, ":", count)
#         h.append(x)
            
        



# # 5. Check if two strings are anagrams
# # Example: "listen" and "silent"



# 6. Remove all white spaces from a string
# str5=input("enter a string: ")
# x1=""
# for x in str5:

#     if x == " ":
#         continue
#     else:
#         x1+=x
# print(x1)



# 7. Find the first non-repeating character in a string
string2="eloolehjhg"
b=''
for x in string2:
    if x not in b:
        count=0
        for c in string2:
            if count==1:
                print(c)
            if x==c:
                count+=1
     

    # count+=1
    # if count==1

# 8. Convert a string to uppercase and lowercase
s = input("Enter string: ")

upper_str = ""
lower_str = ""

for ch in s:
    ascii_val = ord(ch)

    # convert to uppercase
    if 97 <= ascii_val <= 122:  # a-z
        upper_str += chr(ascii_val - 32)
    else:
        upper_str += ch

    # convert to lowercase
    if 65 <= ascii_val <= 90:   # A-Z
        lower_str += chr(ascii_val + 32)
    else:
        lower_str += ch

print("Uppercase:", upper_str)
print("Lowercase:", lower_str)


# 9. Count the number of words in a string


# 10. Find the longest word in a given sentence
s = input("Enter sentence: ")

current_word = ""
longest_word = ""

for ch in s:
    if ch != " ":
        current_word += ch
    else:
        # end of a word
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""

# check last word also
if len(current_word) > len(longest_word):
    longest_word = current_word

print("Longest word:", longest_word)
