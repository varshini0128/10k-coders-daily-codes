import random

rock = '''
                 _    
  _ __ ___   ___| | __
 | '__/ _ \ / __| |/ /
 | | | (_) | (__|   < 
 |_|  \___/ \___|_|\_\
                      
       
        '''
paper = '''
                             
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
       
        '''

scissors = '''
  ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/


            '''

print("welcome to rock-paper-scissors game")
user_value = int(input("choose 0 for rock, 1 for paper, 2 for scissors: "))
# print("you chose: ")
if user_value == 0:
    print(rock)
elif user_value == 1:
    print(paper)
elif user_value == 2:
    print(scissors)
else:
    print("entered incorrect value game over!")
    exit()
print("computer's chose: ")

list2 = [rock, paper, scissors]
choice = random.randint(0, 2)
computer_choice = list2[choice]
print(computer_choice)
#
# if choice == user_value:
#     print("It's a draw match")
# elif choice == 0 and user_value == 1:
#     print("you won!")
# elif choice == 0 and user_value == 2:
#     print("computer won!")
# elif choice == 1 and user_value == 0:
#     print("computer won!")
# elif choice == 1 and user_value == 2:
#     print("you won!")
# elif choice == 2 and user_value == 0:
#     print("you won!")
# elif choice == 2 and user_value == 1:
#     print("computer won!")

# Decide winner
if user_value == choice:
    print("Draw match 🤝")
elif (user_value == 0 and choice == 2) or (user_value == 1 and choice == 0) or (user_value == 2 and choice == 1):
    print("You won 🎉")
else:
    print("Computer won 🤖")








# if user_value == 0 and c == 0:
#     print("draw match")
# elif user_value == 0 and c == 1:
#     print("you won")
# elif user_value == 0 and c == 2:
#     print("you won")
# elif user_value == 1 and c == 1:
#     print("draw match")
# elif user_value == 1 and c == 0:
#     print("computer won")
# elif user_value == 1 and c == 2:
#     print("computer won")
# elif user_value == 2 and c == 0:
#     print("computer won")
# elif user_value == 2 and c == 1:
#     print("you won")
# elif user_value == 2 and c == 2:
#     print("draw match")
