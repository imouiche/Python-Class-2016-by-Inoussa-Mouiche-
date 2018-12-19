# Noughts and crosses

import random

# Variables
#----------
# The board is a two dimensional array
board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]

p1name = ""
p2name = ""
p1symbol = ""
p2symbol = ""
currentTurn = ""
endGame = False
x = 0
y = 0
validMove = False
noOfMoves = 0

# Functions
#----------
def displayBoard(board):
    # We only print the top of the box once
    top_printed = False
    for i in range(3):

        if top_printed == False:
            # Print top of box  
            for j in range(3):                     
                print "+ --",

            print "+"
            top_printed = True

        # Print middle of box            
        for j in range(3):
            print "| ",
            print board[i][j],

        print "|"

        # Print bottom of box
        for j in range(3):
            print "+ --",                

        print "+"

def clearBoard(board):
    # Set all parts of the array to zero
    for row in range(3):
        for col in range(3):
            board[row][col] = " "

def getMoveCoordinates():
    x = int(raw_input("Please type in the row for your move (1-3): "))
    y = int(raw_input("Please type in the column for your move (1-3): "))
    return x, y # return two integers

def checkValidMove(xcoord, ycoord, board):

    # Check xcoord is valid (array begins at 0)
    if xcoord <= 0 or xcoord >3:
        print "Bad row entered"
        return False
    # Check ycoord is valid
    if ycoord <= 0 or ycoord >3:
        print "Bad column entered"
        return False
    # Check if a move has already been made here (-1 because array starts at 0)
    if board[xcoord-1][ycoord-1] == "X" or board[xcoord-1][ycoord-1] == "O":
        print "Someone has already been there!"
        return False

    return True

def checkWin(board):
    someoneHasWon = False

    # Check if someone has got a horizontal row
    for row in range(0,2):
        if (board[row][0] == board[row][1]) and (board[row][1] == board[row][2]) and board[row][0] != " ":
            someoneHasWon = True

    # Check if someone has got a vertical row
    for col in range(0,2):
        if (board[0][col] == board[1][col]) and (board[1][col] == board[2][col]) and board[0][col] != " ":
            someoneHasWon = True

    # Check if someone has got a diagonal row
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and board[0][0] != " ":
            someoneHasWon = True

    # Check if someone has got a diagonal row
    if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and board[1][1] != " ":
            someoneHasWon = True

    return someoneHasWon

def whoStarts():
    rnumber = random.randint(0,100)
    if rnumber %2 == 0:
        return "X"
    else:
        return "O"    

# Main program
#-------------

# Get players to input their name
p1name = raw_input("Enter your name, Player 1: ")
p2name = raw_input("Enter your name, Player 2: ")

# Pick a symbol for player 1
while p1symbol not in ["X", "O"]:
    p1symbol = raw_input("Which symbol would you like "+p1name+"? ")
    if p1symbol not in ["X", "O"]:
        print "You need to pick an X or an O please"

    # Set the P2 symbol
    if p1symbol == "X":
        p2symbol = "O"
    else:
        p2symbol = "X"

print p1name,"is",p1symbol,"and",p2name,"is",p2symbol

# Decide who goes first
currentTurn = whoStarts()
print currentTurn,"is going first. Let's play!"

# Display the board
displayBoard(board)

# Begin the game
while endGame == False:

    print currentTurn,"it is your move"

    # Get an input from the first player
    validMove = False
    while not validMove:
        x,y = getMoveCoordinates()

        # Check whether this move is allowed
        validMove = checkValidMove(x,y,board)
        if validMove:
            # Set this symbol on the board (-1 because of array at 0)
            board[x-1][y-1] = currentTurn
            displayBoard(board)
            noOfMoves += 1

            # Check win or draw
            if checkWin(board):
                print "The winner is",currentTurn,"- congratulations!"
                endGame = True

            elif noOfMoves == 9:
                print "Boring - the game is a draw"
                endGame = True

            # Change the symbol
            if currentTurn == "X":
                currentTurn = "O"
            else:
                currentTurn = "X"
