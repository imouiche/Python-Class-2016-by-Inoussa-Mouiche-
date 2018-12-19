"""Accountants Calculator"""
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
	
	
#	sys.exit()
	
	
#	while type(n1) != int and type(n1)!= float and type(n1) != long:
#	n1 = input("First entry must be anumber: ")
##total += n1

while True:
	n2 = raw_input()
	if n2 in ["*","-","+","/","","quit"]:
		if n2 == "*":
			n3 = input()
			total *= n3
		elif n2 == "+":
			n3 = input()
			total += n3		 
		elif n2 == "-":
			n3 = input()
			total -= n3
		elif n2 == "/":
			n3 = input()
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
	
