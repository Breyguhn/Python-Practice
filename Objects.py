# Creating an object

class Classroom:

	def __init__(self):
		self._people = []

	def add_person(self, person):
		self._people.append(person)

	def remove_person(self, person):
		self._people.remove(person)

	def greet(self):
		for person in self._people:
			person.say_hello()

class Person:

	def __init__(self, name):
		self.name = name

	def say_hello(self):
		print("Hello, ", self.name)

room = Classroom()
room.add_person(Person("Connor"))
room.add_person(Person("Sara"))
room.add_person(Person("Lara"))
room.add_person(Person("Dione"))

room.greet()