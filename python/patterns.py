# for i in range(1,5):
#     for j in range(1,5):
#         if j==1 or i==1 or j==4 or i==4:
#             print('*',end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# print()
# print()

# '''

# *
# **
# ***
# ****
# *****

# ''' 
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end="")
#     print()
# print()

# for x in range(1,6):
#     print("*"*x,end=' ')
#     print()

# print()
# print()

# '''
# *****
# ****
# ***
# **
# *
# '''
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print('*',end="")
#     print()

# print()
# print()

# '''
#      *
#     **
#    ***
#   ****
#  *****
#  '''

# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print('*',end="")
#     print()

# print()
# print()

# '''
#     *
#    ***
#   *****
#  *******
# *********
# '''

# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print('*',end="")
#     print()

# print()
# print()

# '''
# *********
#  *******
#   *****
#    ***
#     *
# '''
# for i in range(5,0,-1):
#     print(" "*(5-i),'*'*i)

# for i in range(5,0,-1):
#     for j in range(5,i,-1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print('*',end="")
#     print()

# print()
# print() 

# '''
#     *
#    ***
#   *****
#    ***
#     *
# '''

# for i in range(1,4):
#     for j in range(3,i,-1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print('*',end="")
#     print()
# for i in range(3,0,-1):
#     for j in range(3,i,-1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print('*',end="")
#     print()

# # 1
# # 0 1
# # 1 0 1
# # 0 1 0 1
# # 1 0 1 0 1

# for i in range(1,6):
#     for j in range(1,i+1):
#         if (i+j)%2==0:
#             print('1',end=" ")
#         else:
#             print('0',end=" ")
#     print()
# print()
# print()

# '''
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# '''

# num=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()

# print()
# print()



# '''
# *
# * *
# * * *
# * *
# *
# '''
# for i in range(1,4):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# for i in range(2,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# S=input()
# s1={}
# for i in S:
#     if i not in s1:
#         s1[i]=1
#     else:
#         s1[i]+=1
# print(s1)

# from itertools import groupby
# S=input()
# for k,g in groupby(S):
#     print(tuple(k,g))
from itertools import groupby

S = input()

for char, grp in groupby(S):
    count = len(list(grp))
    print(f"({count}, {char})", end=" ")
