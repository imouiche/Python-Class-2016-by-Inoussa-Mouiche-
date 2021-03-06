
from __future__ import division
#from math import exp
from scipy.special import gamma
from pylab import exp

def f(x,y):
	return exp(-x*y)

def predictor():
	D = (h**alpha)/gamma(alpha+1)
	E = (h**alpha)/gamma(alpha+2)
	y = [0]
	for j in range(1,N):
		s1 = 0
		s2 = 0
		for k in range(1,j):
			s1 = s1 + b[j-k-1]*f((k-1)*h,y[k-1])
			s2 = s2 + a[j-k]*f(k*h,y[k])
		p = D*s1
		y1 = E*(f(j*h,p)+((j-1)**(alpha+1)-(j-1-alpha)*(j**alpha))*f(0,y[0])+ s2)
		y.append(y1)
	return y

if __name__ == '__main__':
	T = 1
	N = 100
	h = T/N
	alpha = 1/4
	a = []
	b = []
	for k in range(1,N+1):
		b1 = k**alpha - (k-1)**alpha
		a1 = (k+1)**(alpha+1) - 2*(k**(alpha +1)) + (k-1)**(alpha+1)
		a.append(a1)
		b.append(b1)
	Y = predictor()
	print Y
