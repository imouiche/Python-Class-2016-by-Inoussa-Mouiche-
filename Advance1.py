
def vowel():
	vow = 'aeiouAEIOU'
	stence = raw_input(':')
	word = stence.split()
	d = 0
	for w in word:
		W = []
		d += 1 
		P = []
		j = 0
		for i in range(len(w)):
			if w[i] in vow:
				j +=1 
				P.append(i)
				W.append(w[i])
		print '%d word:%s has %d vowels %s at position %s' %(d,w,j, W,P)
