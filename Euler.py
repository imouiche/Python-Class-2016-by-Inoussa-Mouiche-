import pylab as p

def f(y,t):
	return (2-2*t*y)/(t*t +1.0)
	
if __name__=='__main__':
	h = 0.01
	n = int(1.0/h)
	T = [i*h for i in range(n+1)]
	yt = []
	y0 = 1
	Y = [y0]
	for i in range(1,n+1):
		y = Y[i-1] + h*f(Y[i-1], T[i-1])
		Y.append(y)
	p.plot(T,Y)
	p.show()
