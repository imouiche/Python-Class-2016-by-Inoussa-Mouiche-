""" printing subjects and grades of Georges """

if __name__ == '__main__':
	#the given list l of Georges's subjets
	l = [('Math','D'), ('Comp sci', 'B'), ('English','C'), ('French', 'A'),\
 ('Physics','B'), ('History', 'E'), ('Chemistry', 'A')]

	# let's create a dictionnary for easy manipulation

	D = {"Math": 'D', "Comp sci": 'B', "English": 'C', "French": 'A',\
"Physics": 'B', "History": 'E', "Chemistry": 'A'}


	# print out the subjects where Georges has the highest Grades

	for key in D:
		if D[key] == 'A':
			print "Geoges has highest Grades in %s"%key
	#break
		#else:
			#print "Georges doesn't have the highest Grades A in %s:" %key	
	# let's output each objet in a single line
	for key in D:
		print key, ':\t ', D[key]
	for key in D:
		print key.center(8,' '), 
	print '\t'
	for key in D:
		print D[key].center(8,' '),

