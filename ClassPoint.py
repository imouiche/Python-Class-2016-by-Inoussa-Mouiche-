"""define a class """
class Point:
 """2 data members and 2 methods"""
 	def __init__(self,x = 0, y = 0):
 		self.xcoord = x
 		self.ycoord = y
	def fromOrigin(self):
		distance = (self.xcoord**2-self.ycoord**2)**0.5 
		return distance
 	def InUnitcircle(self):
 		self.fromOrigin()<1
 	def __str__(self):
 		return "(%f,%f)" %(self.coord, self.ycoord)
 	
 if __name__=='__main__':
 	pl = Point(1.2,5)
 	d = pl.fromOrigin()
 	print d
