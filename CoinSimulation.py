""" Coin simulation program: Tail appearence probability"""

#||||||||! Import necessary modules |||||||||||||||#
from math import*
from pylab import*
import random
# Definition of the function sucess tail for Num tosses !#
def Successtail(Num):  # Num = number of tosses
	counter = 0   # counter initialization
	h = 0         # heads sucess counter
	tail = 0     # Tail sucess cuonter
	while counter < Num:  
		counter = counter + 1
		rand = random.randint(0,1) # Generate randomly 0 or 1 by toss
		if rand == 1:              # we choise 1 for head
			h = h + 1
		else:                      # 0 correspond to tail sucess
			tail += 1
	return tail                        # return tail

if __name__=='__main__':
###><>>>>>>>> Toss coin and coin a number of times tail has shown <<<<<<<<<<<<<####
	Num = input("Enter number of coin flips:")
	Coin = Successtail(Num)             # Call the function
	print 'The number of teals after num tosses is equal to \t',Coin


#######  Second question: List creation called X #########
#!!!!!! we just called the function and repeat it itterativly 10000 trials #######
	X = [Successtail(Num) for j in range(10000)] 
	print 'List after 10000 trials', X

######### Frequency F(x): For each trial, we count tail shown sucess <############

	freq = [X.count(k) for k in range( Num + 1)] 
	
	Sum = sum(freq)/10000
	print 'The summation of all the frequency is equal to\t ',Sum
####### Histogram and distribution |||||||||||||||||||||||<||||||#############
	bar(range(Num +1), freq, align='center', label =r'Histogram (n=10)') 
	plot(range(Num +1), freq, 'r', linewidth = 2, label =r'Distribution') 
	xlabel('Random variable x')
	ylabel('Frequency F(x)')
	legend()
	title('HISTOGRAM OF DISTRIBUTION: TOSS COIN')
	savefig('Histogram.pdf')
	show()
