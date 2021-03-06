
""" Cryptography using RSK (Rivest Shamir and Adleman)"""

def rap_expo(x, r):
	if r==1:
		return x
	elif r%2==0:
		return rap_expo(x**2,r/2)
	else:
		return x*rap_expo(x**2,(r-1)/2)

# extended euclid algorithm
def egcd(x,y):
	u, v = 0, 1
	m, n = 1, 0
	while x !=0:
		quotient, res = y//x, y%x
		m1= u-m*quotient
		n1= v-n*quotient
		y, x = x,res
		u, v = m,n
		m, n = m1,n1
	return y, u, v  

def modular_inv(x,l):
	d, u, v = egcd(x,l)
	if d!=1:
		return "the inverse of x modulo l does not exist"
	else:
		return u       # public key

def encrypt(p=8191,q=127):
	n = p*q
	phin = (p-1)*(q-1)
	f = open('Mandela.txt','r')
	msg = f.readlines()
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	Alphabet = alphabet.upper()
	out = open('cypherrsk.txt','w')
	i, j, code1, code2 =0,0,{},{}
	for j in xrange(n):
		if egcd(j,n)[0]==1:
			if i<26:
				code1.update({alphabet[i]:j}) 
				code2.update({Alphabet[i]:j}) 
				i+=1
			else:
				code1.update({alphabet[i%26]+str(divmod(i,26)[0]):j}) 
				code2.update({Alphabet[i%26]+str(divmod(i,26)[0]):j}) 
				i+=1
			
	e = 11
	for sentence in msg:
		cypher =''
		i = 0
		while i < len(sentence):
			if (sentence[i] not in alphabet) and (sentence[i] not in Alphabet):
				cypher += sentence[i]
				i +=1
			elif sentence[i] in alphabet:
				k=(rap_expo(code1[sentence[i]],e))%n
				cypher += code1.keys()[code1.values().index(k)]
				i +=1
			else :
				k=(rap_expo(code2[sentence[i]],e))%n
				cypher +=  code2.keys()[code2.values().index(k)]
				i +=1
		out.write(cypher)
	out.close()
	
def decrypt(p=8191,q=127):
	n = p*q
	phin = (p-1)*(q-1)
	f = open('cypherrsk.txt','r')
	msg = f.readlines()
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	Alphabet = alphabet.upper()
	out = open('plaintrsk.txt','w')
	i, j, code1, code2 =0,0,{},{}
	for j in xrange(n):
		if egcd(j,n)[0]==1:
			if i<26:
				code1.update({alphabet[i]:j}) 
				code2.update({Alphabet[i]:j}) 
				i+=1
			else:
				code1.update({alphabet[i%26]+str(divmod(i,26)[0]):j}) 
				code2.update({Alphabet[i%26]+str(divmod(i,26)[0]):j}) 
				i+=1
	e = 11
	d =modular_inv(e,phin)%n
	for m in msg:
		s,al,i,j ='', [],0,0
		while j<len(m):
			k = j+1
			try: 
				int(m[k])
				s += m[j]
				j += 1
			except: 
				s += m[j]
				al.append(s)
				j +=1 
				s = ''
		plaint,t ='', 0
		while t < len(al):
			if al[t] not in code1 and al[t] not in code2:
				plaint += al[t]
				t +=1
			elif al[t] in code1:
				k=(rap_expo(code1[al[t]],d))%n
				plaint += code1.keys()[code1.values().index(k)]
				t +=1
			else: 
				k=(rap_expo(code2[al[t]],d))%n
				plaint += code2.keys()[code2.values().index(k)]
				t +=1
		out.write(plaint)
	out.close()
	
	
