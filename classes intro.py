class Point: #defining class (capitalize the first letters of class)
	def move(self):
		print ('move')

	def draw(self):
		print('draw')
#class defines the blueprint/template for creating an OBJECT!
#to create an object we type the name of our class and then call it like a function 
#this creates a new object and stores it in a variable
point1 = Point()  #point1 object created
point1.draw() #call the point1 object with draw  
point1.x = 10 #setting attributes to the point1 object
point1.y = 20
print(point1.x)