"""Accountants Calculator"""
from __future__ import division
total = 0
n1 = raw_input("Enter a number to start using the calculator: ")
try:
	n1 = float(n1)
	total+=n1
except:
	while True:
		print "First entry must be anumber: "
		n1 = raw_input("Enter a number to start using the calculator: ")
		try:
			n1 = float(n1)
			total+=n1
			break
		except:
			continue

while True:
	n2 = raw_input()
	if n2 in ["*","-","+","/","","quit"]:
		if n2 == "*":
			n3 = raw_input()
			if n3 in ["*","-","+","/","quit"]:
				print total 
				n3 = 1
			else:
				try: n3 = float(n3)
				except:
					print 'Warning,'+'you should enter a number'
					break
			
			total *= n3
		elif n2 == "+":
			n3 = raw_input()
			if n3 in ["*","-","+","/","","quit"]:
				print total 
				n3 = 0
			else:
				try: n3 = float(n3)
				except: 
					
					print 'Warning,'+'you should enter a number'
					break
			total += n3		 
		elif n2 == "-":
			n3 = raw_input()
			if n3 in ["*","-","+","/","","quit"]:
				print total 
				n3 = 0
			else:
				try: n3 = float(n3)
				except: 
					
					print 'Warning,'+'you should enter a number'
					break
			total -= n3
		elif n2 == "/":
			n3 = raw_input()
			if n3 in ["*","-","+","/","","quit"]:
				print total 
				n3 = 1
				
			else:
				try:
					n3 = float(n3)
					if n3==0:
						print 'no division by zero'
						break
				except: 
					
					print 'Warning,'+'you should enter a number'
					break
			total /= n3
		elif n2 == "":
			print "--"
			print total 
		elif n2 == "quit":
			break
	else:
		try:
			n2 = float(n2)	
#	 type(n2) == int or type(n2) == float or type(n2) == long:
			total += n2
		except:
			print "Terrible value. Youre not an intelligent user"
			break
	
