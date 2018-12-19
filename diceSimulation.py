"""Dice simulation"""

import random

def  dice(n,D): #Define the function dice (taking the parameters time 
		#and list of possible outcomes);
	outComesNum = [] #Number of outcome in a fairdice and biased dice;
#Append outcomes after throw in a list (D);
	for i in range(n): 
		num = random.choice(D)
		outComesNum.append(num)
	k = 0 #Initialise counter at 0;
	for i in range(len(outComesNum)): #Count the number of 6 in D;
		if outComesNum[i] == 6:
			k +=1
	return k 

if __name__ == '__main__':
	n = input("Enter the number of throws of dice:\t" )
	fairdice = [1, 2, 3, 4, 5, 6] #List of outcome of fairdice;
	 #List of probability outcome of biasedice;
	biasedice = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6,6]
	rslt1 = dice(n,fairdice) # Number of time of appearance of face 6 for the fair dice;
	print "The number of occurence of 6 in %d throws is: %d" %(n,rslt1)
	rslt2 = dice(n,biasedice)# Number of time of appearance of face 6 for the biase dice.
	print "The number of occurence of biased die of 6 in %d throws is: %d" %(n,rslt2)

