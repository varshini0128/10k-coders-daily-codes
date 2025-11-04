# #Module: It is used to generate pseudo random values.
# #random(): It generates a random float number between 0.0 to 1.0
# import random
# print(random.random())
# #uniform(): It is used to generate random values(float) in specific range 
# print(random.uniform(10,20))
# #randint(): It is used to generate random integer values in specific range
# print(random.randint(1,30))

# #randrange(start,stop,step): It is used to generate random integers with step 
# print(random.randrange(1,20,2))

# #choice(): It is used to choose random value in sequence of values 
# colors=['yellow','red','pink','blue','lavender','black','white','purple','lavender']
# print(random.choice(colors))

# #choices(): It is used to choose multiple values in a sequence, here duplicate values are available 
# #here k is a variable which is a fixed one, we cant use any other variables apart from k 
# print(random.randchoices(colors, k=2)) #include duplicates ex['pink','pink']


# #sample(): It is used to choose random multiple unique values from a sequence of values 
# print(random.sample(colors,k=2))  #doesnot include duplicates 


# #shuffle(): It is used to shuffle a list randomly
# cards=['Jack','king','queen','Ace','1','2','3','4','5','6','7','8','9','10']
# random.shuffle(cards)
# print(cards)


def folded_sheet():
    R, C = map(int, input().split())
    instructions = input().split()

    # Create initial sheet with stacks
    sheet = [[[r * C + c + 1] for c in range(C)] for r in range(R)]

    for inst in instructions:
        if inst[0] == 'h':  # horizontal fold
            k = int(inst[1:]) - 1
            top = sheet[:k+1]
            bottom = sheet[k+1:]
            bottom.reverse()
            for i in range(len(bottom)):
                for j in range(len(bottom[0])):
                    top[-1 - i][j] = bottom[i][j] + top[-1 - i][j]
            sheet = top

        elif inst[0] == 'v':  # vertical fold
            k = int(inst[1:]) - 1
            left = [row[:k+1] for row in sheet]
            right = [row[k+1:] for row in sheet]
            for r in right:
                r.reverse()
            for i in range(len(sheet)):
                for j in range(len(right[0])):
                    left[i][-1 - j] = right[i][j] + left[i][-1 - j]
            sheet = left

    final_stack = sheet[0][0]
    print(final_stack[0], final_stack[-1])
folded_sheet()