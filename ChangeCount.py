
def changtoCount(n):
	x = list(input('please enter your list:'))
	#l = set(L)
	k = 0
	while k <= n:
		y = []
		for i in range(len(x)):
			c = 0
			for l in x:
				if l == i:
					c += 1
			y.append(c)
		x = y
		print x
		k +=1
		
def Float():
	x = list(input('please enter your list:'))
	X = [float(el) for el in x]
	return X
def Polynom():
	L = list(input('please enter your list:'))
	L.reverse()
	n = len(L)-1
	p = ''
	poly = []
	d = 0
	for a in L:
		if a != 0:
			if n-d==0:
				p =  p + '+' + str(a)
				d = d+1
			elif n-d ==1:
				p =  p + '+' + str(a)+'x'
				d = d +1
			else:
				p =  p + '+' + str(a)+'x^'+str(n-d)
				d = d +1
		else: 
			d = d+1
		#poly.append(p + '+')
	print p
def poly(l, x):
	n=0
	valp = 0
	for coef in l:
		valp = valp + (coef * (x**n))
		n += 1

	return valp



