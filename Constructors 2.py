class Person:
	def __init__(self, name):
		self.name = name
	def talk(self):
		print(f'Hi my name is {self.name} lets chat')


John = Person('Johny Smith')
John.talk()

Ilja = Person('Ilja Solovjev')
Ilja.talk()