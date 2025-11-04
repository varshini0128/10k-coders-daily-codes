#write a code to simulate ludo game

import random
players_count=int(input('Enter no of players: '))
if players_count>4 or players_count==1:
    print('cant play')
elif players_count==4:
    player1=input('Enter Player1 Name:')
    player2=input('Enter Player2 Name:')
    player3=input('Enter Player3 Name:')
    player4=input('Enter Player4 Name:')
elif players_count==3:
    player1=input('Enter Player1 Name:')
    player2=input('Enter Player2 Name:')
    player3=input('Enter Player3 Name:')
elif players_count==2:
    player1=input('Enter Player1 Name:')
    player2=input('Enter Player2 Name:')
# print(player1,'roll dice')

continue_game=''
# game='True'
value=0
new_value=0
new_value2=0
def player():
 while True:
        value=random.randint(1,6)
        if value==6:
            print(player1,' got 6, roll again')
            print('play again')
            new_value=random.randint(1,6)
            print('you rolled a value: ', new_value)
            value+=new_value
            print(player1,', your total score is ',value)
            print('It is your turnn',player2)
            # player_2()

           
        else:
           print(player1,'you got',value,', Try Again')
           print('It is your turn',player2)
        
        return

    


def player_2():
    while True:
        value=random.randint(1,6)
        if value==6:
            print(player2,' got 6, roll again')
            print('play again')
            new_value2=random.randint(1,6)
            print('you rolled value: ', new_value2)
            value+=new_value2
            print(player2,', your total score is ',value)
            break
        else:
           print('you got',value,', Try Again')
           print('It is your turn',player1)
        # player()
        return
# player()

player2_turn=1
player1_turn=1
for players_turn in range(1,53):
    if player1_turn%2!=0:
        player()
        player2_turn+=1
    else :
        player_2()
        player1_turn+=1
print(new_value)
print(new_value2)


# continue_game=input('do you want to continue? y/n: ')
# if continue_game=='y':
#     game_enter()
#     if game_enter()=='True':
#         print('hi')
        
        

# # game_enter()


    


    


# def roll_dice():
#     if game_enter()==6:
#         game_enter()
    