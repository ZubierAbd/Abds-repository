import random

import sys

def drawboard(board):
    #draw the board structure

    hline = '   ' #initial space for the numbers

    for i in range(1,6):
        hline += (' ' * 9) + str(i)