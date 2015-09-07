class Parent(object):
	
	def override(self):
		print "Parent override()"

class Child(Parent):

	def override(self):
		print "Child override()"

son = Child()
dad = Parent()

son.override()
dad.override()