# # # # a = 12
# # # # b = 18

# # # # great = a if a > b else b

# # # # while True:
# # # #     if great % a == 0 and great % b == 0:
# # # #         print(great)
# # # #         break
# # # #     great += 1
# # # # print(36%12==0 and 36%18==0)


# # # n = 12345
# # # count = 0
# # # while n > 0:
# # #     count += 1
# # #     n //= 10
# # # print(count)



# # # n = 10
# # # count = 0
# # # i = 5
# # # while i <= n:
# # #     count += n // i
# # #     i *= 5
# # # print(count)


# # arr = [1, 2, 3, 4, 5]
# # n = 2
# # res = []

# # for i in range(n, len(arr)):
# #     res.append(arr[i])
# # for i in range(0, n):
# #     res.append(arr[i])

# # print(res)


# # arr = [0, 1, 0, 3, 12]
# # res = []

# # for x in arr:
# #     if x != 0:
# #         res.append(x)

# # zeros = []

# # for x in arr:
# #     if x == 0:
# #         zeros.append(x)

# # print(res + zeros)


# arr = [1, 2, 4, 5]
# n = 5
# total = 0

# # sum 1..n manually
# s = 0
# for i in range(1, n + 1):
#     s += i

# for x in arr:
#     total += x

# print(s - total)


table = [[i*j for j in range(1,4)] for i in range(1,4)]
print(table)
m=[]
n=[]
for i in range(1,4):
    for j in range(1,4):
        n=[i*j]

    m.append(n)
# m.append(n)
print(m)
alphabets = [chr(i) for i in range(65, 91)]
print(alphabets)
pal = [i for i in range(1,101) if str(i) == str(i)[::-1]]
print(pal)