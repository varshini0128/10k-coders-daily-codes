rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2*i - 1))

rows = 5
for i in range(rows, 0, -1):
    print("*" * i)
