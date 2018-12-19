"""class person"""

class Person:
	def __init__(self, Name, Surname):
		self.name = Name
		self.surname = Surname
	def __str__(self):
		return "%s %s" %(self.name, self.surname)
	def Getsurname(self):
		print self.surname
class Student(Person):
	def __init__(self, Name, Surname, StudNumber):
		Person.__init__(self.name, Surname)
		self.StudentNumber = StudNumber
		
	def GetStudentNumber(self):
		print self.studentNumber
		
if __name__ =='__main__':
	P = Person('John','Legend')
	print P
	P.GetSurname()
	stud = Student('john',  'Bakon', '1425')
	print stud
	stud.GetSurname()
	stud.GetStudNumber()
	
	
	
