class Student(object):
	def __init__(self, name, fave_food, fave_color, current_grade):
		self.name = name
		self.fave_food = fave_food
		self.fave_color = fave_color
		self.current_grade = current_grade

	def setGrade(self, new_grade):
		self.current_grade = new_grade

myKarla = Student("Karla", "Turbos", "blue", "A")
myJose = Student("Jose", "pizza", "green", "A")
myKahlil = Student("Kahlil", "cheeseburger", "green", "B")

print(myKahlil.fave_food)
myKahlil.fave_food = "tacos"
print(myKahlil.fave_food)
