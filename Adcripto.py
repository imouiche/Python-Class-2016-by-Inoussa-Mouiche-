""" Cryptography using Ceasar method """
def crypto():
	f = open('aims.txt','r')
	msg = f.readlines()
	k = input('enter your key ')
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	out = open('cyphertxt.txt','w')
	for sentence in msg:
		cypher =''
		i = 0
		while i < len(sentence):
			k +=1 
			if sentence[i] not in alphabet and sentence[i] not in Alphabet:
				cypher += sentence[i]
				i +=1
			elif sentence[i] in alphabet:
				j =alphabet.index(sentence[i])
				cypher += alphabet[(j+k)%26]
				i +=1
			elif sentence[i] in Alphabet:
				j = Alphabet.index(sentence[i])
				cypher += Alphabet[(j+k)%26]
				i +=1
			else:
				i +=1
		out.write('%s' %cypher)
		
	out.close()
	#return cyphertxt

def decrypt():
	f = open('cyphertxt.txt','r')
	msg = f.readlines()
	k = input('enter your key ')
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	out = open('plaintxt.txt','w')
	for sentence in msg:
		plaint =''
		i = 0
		while i < len(sentence):
			k +=1 
			if sentence[i] not in alphabet and sentence[i] not in Alphabet:
				plaint += sentence[i]
				i +=1
			elif sentence[i] in alphabet:
				j =alphabet.index(sentence[i]) 
				plaint += alphabet[(j-k)%26]
				i +=1
			elif sentence[i] in Alphabet:
				j = Alphabet.index(sentence[i])
				plaint += Alphabet[(j-k)%26]
				i +=1
			else:
				i +=1
		out.write('%s' %plaint)
		
	out.close()
