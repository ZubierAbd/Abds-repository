print('Prepare yourself for Sonar')

import random

import sys

def drawboard(board):
    hline = '   '
    for i in range(1,6):
        hline += ('  '* 9) + str(i)

    print(hline)
    print('    ' + {'0123456789' * 6})
    print()

    #print each of the 15 rows
    for i in range(15):
        #single digit numbers need to be padded with an extra space

        if i < 10:
            extraspace = ' '
        else:
            extraspace =''
        print('%s %s %s' % (extraspace,i,getrow(board,i),i))
        #print the numbers across the bottom
        print()
        print('   ' + ('0123456789' * 6))
        print(hline)

def getrow(board,row):
    #return a string from a board data structure at a certain row
    boardrow = ' '
    for i in range(60):
        boardrow += board[i][row]
    return boardrow

def getnewboard():
    board = []
    for x in range(60): #the main list is a list of 60 lists
        board.append([i])

        for y in range(15):
            if random.randint(0,1) == 0:
                board[x].append('-')
            else:
                board[x].append('~')

    return board

def getrandomchests(numchests):
    #create a list of chest data structures (two item lists of x,y coordinates)

    chests = []
    for i in range(numchests):
        chests.append([random.randint(0,59),random.randint(0,14)])
    return chests

def isvalidmove(x,y):
    #return true if coordinates are on the board
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makemove(board):
    if not is validmove(x,y):
        return False

    smallestdistance = 100

    for cx,cy in chests:
        if abs(cx-x) > abs(cy - y):
            distance = abs(cx-x)
        else:
            distance = abs(cy-y)

        if distance <smallestdistance:
            smallestdistance = distance

        if smallestdistance == 0:
            chests.remove([x,y])
            return 'You have found a sunken treasure chest'
        else:
            if smallestdistance <10:
                board[x,y] = str(smallestdistance)
                return 'Treasure detected at a distance of %s from the sonar' %(smallestdistance)
            else:
                board[x][y] = 'O'
                return 'Sonar did not detect anything. ALl treasure chests out of range'
