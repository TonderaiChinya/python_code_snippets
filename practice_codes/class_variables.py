class Student:

	studentIdNumber = 100

	def __init__(self, studentName, studentSurname, studentClass):
		self.studentName = studentName
		self.studentSurname = studentSurname
		self.studentClass = studentClass
		self.studentFullname = self.studentName + ' ' + self.studentSurname

		Student.studentIdNumber += 1

	def fullname(self):
		return '{} {}'.format(self.studentName, self.studentSurname)

std1 = Student('Tony', 'Clemz', 'Science')

print(std1.fullname())
print(std1.studentIdNumber)