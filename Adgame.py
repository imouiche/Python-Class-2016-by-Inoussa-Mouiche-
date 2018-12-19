""" Draw table using Python """
import random

def Drawsquare():
	global n
	for i in range(n):

		if i<1:
			for j in range(n):  
				print "+ --",

			print "+"

		for j in range(n):
			print "|   ",
			#print board[i][j],

        	print "|"

		for j in range(n):
			print "+ --",

		print "+"

def Empty(Str):
	for row in range(n):
		for col in range(n):
			Str[row][col] = " "
def Position():
	x = abs(int(raw_input("Enter your x coordinate (1-%d): "%n) or "10"))
	y = abs(int(raw_input("Enter your y coordinate (1-%d): "%n) or "10"))
	return x, y

def validposition(x,y,l):
	if x<= 0 or x>n:
		print "please enter your row between 0 and %d"%n
		return False
	if y<= 0 or y >n:
		print "please enter your column between 0 and %d"%n
		return False
	if l[x-1][y-1] == "X" or l[x-1][y-1] == "O":
		print "this position is occupied"
		return False
	return True

def Win(l):
	winingtest = False

	for row in range(0,2):
		if (l[row][0] == l[row][1]) and (l[row][1] == l[row][2]) and l[row][0] != " ":
			winingtest = True

	for col in range(0,2):
		if (l[0][col] == l[1][col]) and (l[1][col] == l[2][col]) and l[0][col] != " ":
			winingtest = True

	# Check if someone has got a diagonal row
	if (l[0][0] == l[1][1]) and (l[1][1] == l[2][2]) and l[0][0] != " ":
		winingtest = True

	# Check if someone has got a diagonal row
	if (l[0][2] == l[1][1]) and (l[1][1] == l[2][0]) and l[1][1] != " ":
		winingtest = True

	return winingtest

def whobegins():
	rnumber = random.randint(0,100)
	if rnumber %2 == 0:
		return "X"
	else:
		return "O"    

def Play():
	global n
	n =int(raw_input('please enter the size of your square: '))# size of the table
	l = [""*i for i in range(n)]
	l = [l]*n
	p1name = raw_input("Player 1, enter your name: ")
	p2name = raw_input("Player 2, enter your name: ")
	p1symbol = ""
	p2symbol = ""
	currentTurn = ""
	endGame = False
	x = 0
	y = 0
	validMove = False
	noOfMoves = 0

# Pick a symbol for player 1
	while p1symbol not in ["X", "O"]:
		p1symbol = raw_input("Which symbol would you like "+p1name+"? ")
		if p1symbol not in ["X", "O"]:
			print "You need to pick an X or an O please"

		if p1symbol == "X":
			p2symbol = "O"
		else:
			p2symbol = "X"

	print p1name,"is",p1symbol,"and",p2name,"is",p2symbol
	
	# Decide who goes first
	currentplayer = whobegins()
	print currentplayer,"is going first. Let's play!"

	# Display the board
	#displayBoard(board)
	Drawsquare()
	# Begin the game
	while endGame == False:

		print currentplayer,"it is your move"

		# Get an input from the first player
		validMove = False
		while not validMove:
			x,y = Position()

			# Check whether this move is allowed
			validMove = validposition(x,y,l)
			if validMove:
			# Set this symbol on the board (-1 because of array at 0)
				l[x-1][y-1] = currentplayer
				#displayBoard(board)
				Drawsquare()
				noOfMoves += 1

			# Check win or draw
				if Win(l):
					print "The winner is",currentplayer,"- congratulations!"
					endGame = True

				elif noOfMoves == 9:
					print "Boring - the game is a draw"
					endGame = True

			# Change the symbol
				if currentplayer == "X":
					currentplayer = "O"
				else:
					currentplayer = "X"

	#print T
	

