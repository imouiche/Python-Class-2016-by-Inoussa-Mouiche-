""" Cryptography using Viginere method """

def key(msg,k):
	code = ''
	j=0
	while j < len(msg):
		code += k[j%len(k)]
		j +=1
	return code 


def Vigcryto():
	f = open('Mandela.txt','r')
	msg = f.readlines()
	k = raw_input('enter your key ')
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	out = open('cyphertxtvig.txt','w')
	for sentence in msg:
		codage = key(sentence,k)
		print codage
		cypher = ''
		i = 0
		while i < len(sentence):
			if sentence[i] not in alphabet and sentence[i] not in Alphabet:
				cypher += sentence[i]
				i +=1
			elif sentence[i] in alphabet:
				s = alphabet.index(sentence[i]) + alphabet.index(codage[i])
				cypher += alphabet[s%26] # lower coding
				i +=1
			elif sentence[i] in Alphabet:
				s = Alphabet.index(sentence[i]) + Alphabet.index(codage[i].upper())
				cypher += Alphabet[s%26] # upper coding
				i +=1
			else:
				i +=1
		out.write(cypher)
	out.close()
	
def decoVig():
	f = open('cyphertxtvig.txt','r')
	msg = f.readlines()
	k = raw_input('enter your key ')
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	out = open('plaintxtvig.txt','w')
	for sentence in msg:
		codage = key(sentence,k)
		plaintxt = ''
		ii = 0
		while ii < len(sentence):
			if sentence[ii] not in alphabet and sentence[ii] not in Alphabet:
				plaintxt += sentence[ii]
				ii +=1
			elif sentence[ii] in alphabet:
				s = alphabet.index(sentence[ii]) - alphabet.index(codage[ii])
				plaintxt += alphabet[s%26] # lower coding
				ii +=1
			elif sentence[ii] in Alphabet:
				s = Alphabet.index(sentence[ii]) - Alphabet.index(codage[ii].upper())
				plaintxt += alphabet[s%26] # upper coding
				ii +=1
			else:
				ii +=1
		out.write(plaintxt)
		print plaintxt
	out.close()
		 
	
	
	
	
	
