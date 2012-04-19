"""
pet.py
=====
Create a class called Pet, subclass it to create a Dog and Cat class

Pet will have a speak and speak_twice method, as well as a name attribute that is initialized in a constructor.

Example Output:
>>> p = pet.Pet("mojo")
>>> print p
mojo
>>> p.speak()
generic animal talk
>>> p.speak_twice()
generic animal talk
generic animal talk
>>> c = pet.Cat("mittens")
>>> print c
mittens
>>> c.speak_twice()
meow
meow
>>> 
"""

class Pet:
	def __init__(self, name):
		self.name = n
	def __str__(self):
		return self.name
	def speak(self):
		print "generic animal sounds"

class Dog(Pet):
	def speak(self):
		print "barK"

class Cat(Pet):
	def speak(self):
		print "nyan"


p = Pet("fluffy")
print p 
d = dog("spot")
print d