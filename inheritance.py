class Mammals:
	def __init__(self, name):
		self.name = name
	def talk(self):
		print(f'Hi my name is {self.name} lets chat')




class Cat(Mammals): #inherits methods from the mammals class
	def meow(self):
		print("meaowww")


class Dog(Mammals):
	def bark(self):
		print('ruff-fuff')

cat1 = Cat('Pussy')
cat1.meow()
print(cat1.name)
cat1.talk() # calls inherited function

dog1 = Dog('Neja')
dog1.bark()
dog1.talk()
