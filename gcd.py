""" comput the greatest common divisor"""
import sys

def gcd():
	print 'this program computes the greatest common divisor between two numbres'
	a,b = input('Please enter two numbers:')

	if a > b:
		n = b
	elif a < b:
		n = a
	else:
		print("The  gcd. of", a,"and", b,"is", a)
	
	for i in range(1, n + 1):
		if((a % i == 0) and (b % i == 0)):
			gcd = i

	return gcd

	print("The  gcd. of", a,"and", b,"is", gcd(a, b))

def GCD(a,b):
	if a<b: a,b = b,a
	while b>0:
		a,b = b, a%b
	return a
if __name__=='main':
	try:
		a = int(sys.argv[1])
	except:
		print "please we accept anly integers: Check the first entry "
	sys.exit(1)
	try:
		b = int(sys.argv[2])
	except:
		print "please we accept anly integers: Check the first entry "
	sys.exit(2)
	b = int(sys.argv[2])
	print "The gcd(%d,%d) = %d"%(a,b gcd(a,b))
