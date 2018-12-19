""" factorial"""
import sys

def facto(n):
	#recorder = sys.stdout
	#f = file('factorial.output.txt','w')
	#sys.stdout = f
	fact = 1
	for i in range(1, n+1):
		fact = fact*i
		#v = fact
	return fact
	#print ("factorial of {} is {} ".format(n, fact))
	#sys.stdout = recorder
	#f.close()
		
