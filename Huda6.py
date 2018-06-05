import random

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputplayerletter():
    letter = ''
    while not  (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O? ')
            letter = input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whogoesfirst():
    if (random.randint(0,1) == 0):
        return 'computer'
    else:
        return 'player'

def playagain():
    print('Do you want to play again?')
    return input().lower().startswith('y')

def makemove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getboardcopy(board):
    dupeboard = []

    for i in board:
        dupeboard.append(i)

    return dupeboard

def isspacefree(board, move):
    return board[move] == ''

def getplayermove(board):
    move = ' '
    while (move not in '1 2 3 4 5 6 7 8 9'.split() or not isspacefree(board, int(move))):
        print('what is your next move')
        move = input()
    return int(move)

def chooserandommovefromlist(board,movelist):
    possiblemoves = []
    for i in moveslist:
        if (isspacefree(board,i)):
            possiblemoves.append(i)
        if len(possiblemoves!=0):
            return random.choice(possiblemoves)
        else:
            return none

def getComputermove(board,computerletter):
    if(computerletter == 'O'):
        playerletter = 'X'
    else:
        playerletter = 'O'

    for i in range(1,9):
        copy = getboardcopy(board)
        if (isspacefree(copy,i)):
            makemove(copy,computerletter,i)
            if (isWinner(bo,le)):
                return i

    for i in range(1,9):
        copy = getboardcopy(board)
        if (isspacefree(copy,i)):
            makemove(copy,playerletter,i)
        if (isWinner(copy,playerletter)):
            return i

    move = chooserandommovefromlist(board,[1,3,5,7])

    if (move != None):
        return move

    if(isspacefree(board,5)):
        return 5

    return chooserandommovefromlist(board, [2,4,6,8])

def isboardfull(board):
    for i in range(1,10):
        if isspacefree(board,i):
            return False
        else:
            return True

print('Welcome to Tic Tac Toe')

while(True):

    theboard = ['']*10
    playerletter,computerletter = inputplayerletter()
    turn = whogoesfirst()
    print('The ' + turn)
    gameisplaying = True

    while(gameisplaying):
        if (turn == 'player'):
            drawBoard(theboard)
            move = getplayermove(theboard)
            makemove(theboard,playerletter,move)

            if (isWinner(theboard,playerletter)):
                drawboard(theboard)
                print('Hoorray you are the winner')
                gameisplaying = False
            else:
                if (isboardfull(theboard)):
                    drawboard(theboard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputermove(theboard, computerletter)
            makemove(theboard, computerletter,move)
            if (isWinner(theboard, computerletter)):
                drawboard(theboard)
                print('The computer has beaten you')
                gameisplaying = False
            else:
                if (isboardfull(theboard)):
                    drawboard(theboard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'player'

        if (not playagain()):
            break
