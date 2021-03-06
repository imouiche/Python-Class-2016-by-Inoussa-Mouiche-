""" Binomial to normal distribution"""

from __future__ import division # help avoid mistake for integer division

import pylab as pl
import random
import math as m
import numpy as np

def gaussian(x, mu, sigma):
	"""return the value of the gaussian function"""
	y = 1./np.sqrt(2*m.pi*sigma**2)*np.exp(-(x - mu)**2/(2*sigma**2))
	
	return y
	

if __name__=='__main__':
	
	succes = 0
	i = 1
	j = 1
	N = 1000
	p = 1./6. #probability to have six-faced 
	q = 1-p  # probability of failure 
	n = 100
	y=[]
	# loop over 1000 exp

	while i <= N:
		# Loop over 100 tosses

		for j in range(1,n+1):
			# Toss the dice
			D = random.randrange(1,7)
			if D == 6:
				succes = succes +1
			else:
				succes  = succes
	
		y.append(succes)

		i = i +1
		succes=0
	

	mu = n*p
	sigma = n*p*q 

	
	x = np.linspace(0,100,1000)
	
	y1 = 1/m.sqrt(2*m.pi*sigma**2)*np.exp(-(x-mu)**2/2*sigma**2)
	


	pl.hist(y,bins=100)              # plot the first function with red (r) dashed lines (-)
	pl.hold('on')
	pl.plot(x, 8000*y1, 'r-')              # plot the second function with blue (b) circles (o)
	pl.xlabel('t')
	pl.ylabel('y')
	pl.legend(['gaussian','histogram'])
	pl.title('Plotting two curves in the same plot')
	pl.savefig("binomialToGaussian.png")       #figure will be saved in current working directory
	pl.show()
			
