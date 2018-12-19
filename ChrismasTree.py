""" drawing a Chrismas Trees"""

if __name__ == '__main__':
	name = raw_input(" How can I call you ?")
	N = input("yes Mr %s,enter an integer: "%name) # prompt user to enter the integer value of N
	
	j = -1 # initialization of counter
	asterist = '*' # define aasterisks
	for i in range(N):
		j = j+ 2  # fixe the odd numbers
		a = asterist*j # number of asterisks to be printed
		print 20*' ', a.center(2*N," ") # center and print      the ith line asterisks
	print 20*' ', '*'.center(2*N," ") # center and print the two last line 
	print 20*' ', '*'.center(2*N," ")

