import numpy as np
import pylab
import cv2
import AffineTransfoMatrix
#import mahotas as mh
import matplotlib.pyplot as plt

I = cv2.imread('dna.jpeg')
#I = cv2.imread('aims2.jpg')
I = cv2.imread('messi.jpg')
print (I.shape[:2])
im = AffineTransfoMatrix.resize(I, height = 300) # scaling
#gray = cv2.GaussianBlur(im, (5, 5), 0) # bluring with 0 as standard deviation in X and Y direction
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(im, 20, 100)# detect edged of the image with h and w boundary

print (im.shape)
print (im.dtype)
print (I.max())
print (I.min())

(_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
# loop over the contours
print (len(cnts))
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	print (approx)
	# if our approximated contour has four points, then we
	# can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break

# show the contour (outline) of the piece of paper
print ("STEP 2: Find contours of paper")
print (im.shape)
cv2.drawContours(im, [screenCnt], -1, (0, 255, 0), 2)
plt.imshow("Outline", im)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#plt.imshow(I)
plt.imshow(edged)
pylab.gray()
plt.show()

