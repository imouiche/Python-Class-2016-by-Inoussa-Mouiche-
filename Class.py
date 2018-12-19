 
class Cplx:
	def __init__(self, a=0,b=0):
		self.real = a
		self.img = b
		
	def __str__(self):
		
		return "%f + %fi" %(self.real, self.img)if self.img>0 else "%f - %fi" %(self.real, -self.img)
	#def add(self,c): # to be defined during dinner
	def add(self, x):
		return Cplx(self.real + x.real, self.img + x.img)
	def __add__(self, x):
		return Cplx(self.real + x.real, self.img + x.img)
	def __sub__(self, x):
		return Cplx(self.real - x.real, self.img - x.img)       

	def __mul__(self, x):
		return Cplx(self.real*x.real - self.img*x.img,self.real*x.img + self.img*x.real)  
	
	#def __add__(self): # to be defined after dinner
	def __abs__(self):
		return (self.real**2 + self.img**2)**.5
	def _abs(self):
		return (self.real**2 + self.img**2)**.5
	
class Polynomial:
	def __init__(self, List1_coeffs):
		self.coeff = List1_coeffs
	def __str__(self):
		#self.coef = coefs
		#y = 'x'
		self.coeff.reverse()
		l = len(self.coeff)
		d = 0
		deg = [l-i for i in range(1 ,l)]
		p = ''
		D = []
		n = l-1
		for a in self.coeff:
			if a != 0 and a <0:
				if n-d==0:
					p =  p + str(a)
					d = d+1
				elif n-d ==1:
					p =  p  + str(a)+'x'
					d = d +1
				else:
					p =  p  + str(a)+'x^'+str(n-d)
					d = d +1
				D.append(d)
			elif a!=0 and a> 0:
				if n-d==0:
					p =  p + '+'+str(a)
					d = d+1
				elif n-d ==1:
					p =  p  + '+'+ str(a)+'x'
					d = d +1
				else:
					p =  p  + '+'+ str(a)+'x^'+str(n-d)
					d = d +1
				D.append(d)
			else:
				d = d+1
				D.append(d)
			#poly.append(p + '+')
		return p
	def __len__(self):
		return len(self.coeff)

#--------------Evaluate the polynomial------------
	def __call__(self, x):
		Eval = 0
		for i in range(len(self.coeff)):
			Eval += self.coeff[i]*(x**i)
		return Eval
	def __getitem__(self,i):
		return self.coeff[i]

	def __add__(self, List2_coeffs):
	# Start with the longest list and add in the other
		l1 = len(self.coeff)
		l2 = len(List2_coeffs)
		if l1 > l2:
			poly.coeff = self.coeff[:]  # copy!
			for i in range(l2):
				poly.coeff[i] += List2_coeffs[i]
		else:
			poly.coeff = List2_coeffs[:] # copy!
			#poly.coeff = List2_coeffs # copy!
			for i in range(l1):
				poly.coeff[i] +=  self.coeff[i]
		return Polynomial(poly.coeff)
	
if __name__ =='__main__':
	p = Cplx(-1,10)
	q = Cplx(2,3)
	s = p-q
	m = p*q
	#print 'their sum is ', s, 'and their multiplication is', m
	#print p._abs(), abs(p)
	L = [-1,-4,2,0]
	l = [4,5,6,2]
	poly1 = Polynomial(l)
	poly = Polynomial(L)
	print poly1+ poly
	
	
