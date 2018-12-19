def encript():
	f = open('Mandela.txt','r')
	msg = f.readlines()
	k = input('enter your key ')
	alphabet = 'abcdefghijklmnopkrstuvwxyz'
	Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	plaintxt = ''
	out = open('plaintxt.txt','w')
	for sentence in msg:
		plaintxt = ''
		for i in range(len(sentence)):
			j = 0
			while len(plaintxt)==0 and j < len(alphabet)):
				if sentence[i]==alphabet[j]:
					plaintxt += alphabet[(j+k)%26]
					
				elif sentence[i]==Alphabet[j]:
					plaintxt += Alphabet[(j+k)%26]
				elif sentence[i]== ' ':
					plaintxt += ' '
				else :
					plaintxt += sentence[i]
				#break
				j = j+1
			print i
		out.write(plaintxt)
