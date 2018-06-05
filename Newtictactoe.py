import random
import os

def displayboard(board):
    clearoutput()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def clearoutput():
     print('\n'*100)
    # os.system('cls')

def playerinput():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Please input X or O").upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O')


def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[7] == board[5] == board[3] == mark)

def choose_first():
    a = random.randint(0,1)
    if a == 0:
        return 'Player One'
    else:
        return 'Player Two'

def space_check(board,position):
    return board[position] == ' '

def fullboard(board):
    for i in range(1,10):
       if space_check(board,i):
           return False

    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position'))

    return position

def replay():
    choice = input('Play again? Enter yes or no')
    return choice == 'Yes'


print('Welcome to Tic Tac Toe ')

while True:

    theboard =[' ']*10
    player1_marker,player2_marker = playerinput()

    turn = choose_first()
    print(turn + 'Will go first')

    playgame = input('Ready to play?')

    if playgame == 'y' or 'Y':
        game_on = True
    else:
        gane_on = False

    while game_on:
        if turn == "Player One":
            displayboard(theboard)
            position = player_choice(theboard)
            place_marker(theboard,player1_marker,position)
            if win_check(theboard,player1_marker):
                print('Player 1 has won')
                game_on = False
            else:
                if fullboard(theboard):
                    displayboard(theboard)
                    print('THE GAME IS A TIE')
                    break
                else:
                    turn = 'Player Two'

        else:
            displayboard(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)
            if win_check(theboard, player2_marker):
                print('Player 2 has won')
                game_on = False
            else:
                if fullboard(theboard):
                    displayboard(theboard)
                    print('THE GAME IS A TIE')
                    break
                else:
                    turn = 'Player One'



    if not replay():
        break