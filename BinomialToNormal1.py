""" Binomial to normal distribution"""

from __future__ import division 

import pylab as pl
import random
import math as m
import numpy as np


def gaussian(x, mu=0, sigma=1):
	"""Return the value of the Gaussian function at x"""
	y = 1/np.sqrt(2*m.pi*sigma**2)*np.exp(-(x - mu)**2/(2 *sigma**2))
	return y


if __name__=='__main__':
	
	succes = 0
	i = 1
	j = 1
	N = 1000
	p = 1./6
	q = 1-p
	n = 100
	y=[]

	while i <= N:

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
		
	h = 1 # larger of one histogram

	q = 1-p
	w = N*h # area to close/match two curves in the same figure 
	
	x = np.linspace(0,50,1000) 
	y1 = gaussian(x, n*p, m.sqrt(n*p*q))

	pl.hist(y,bins=100)           
	pl.hold('on')
	pl.plot(x, y1, 'r-', markersize = 1,linewidth = 4)              
	#pl.xlabel('t')
	#pl.ylabel('y')
	pl.legend(['gaussian','histogram'])
	pl.title('Approximation of ')
	pl.savefig("binomialToGaussian.png")       
	pl.show()
			
