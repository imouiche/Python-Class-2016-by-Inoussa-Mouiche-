"""Box u = 1 contains 1 red ball and 3 black balls. 
Box u = 2 contains 1 red ball, 1 white ball, and 1 black
ball. Box u = 3 contains 1 red ball and 1 black ball."""

from __future__ import division
from random import *

if __name__=="__main__":

	S = 0
	box1 = 0
	box2 = 0
	box3 = 0
	trial = 10000
	for n in range(trial):
		b1 = ['r','b','b','b'] # r = red, b= black, w = white
		b2 = ['r','w','b']
		b3 = ['r','b']

		k = [b1,b2,b3]
		l = choice(k)
		m = choice(l)
# The probability of choosing a red ball from any randomly choosen box
		if m=='r': 
			S+=1
			ChanceOfRed= S/trial

		if choice(b1)=='r': #probability of choosing red from box 1
			box1+=1
			chanceOfRed1 = (box1/trial)
#			print chanceOfRed1

		if choice(b2)=='r': #probability of choosing red from box 2
			box2 +=1
			chanceOfRed2 = (box2/trial)
#			print chanceOfRed2

		if choice(b3)=='r': #probability of choosing red from box 3
			box3 +=1
			chanceOfRed3 = (box3/trial)
#			print chanceOfRed3
print 'The prob. of choosing RED Ball from any of the box is %f, ExactSol:  %f' %(ChanceOfRed, 13/36)
print 'The prob. of choosing RED ball from Box1 is %f, ExactSol:  %f' %(chanceOfRed1, 3/13)
print 'The prob. of choosing RED ball from Box2 is %f, ExactSol:  %f' %(chanceOfRed2, 4/13)
print 'The prob. of choosing RED ball from Box3 is %f, ExactSol:  %f' %(chanceOfRed3, 6/13)

