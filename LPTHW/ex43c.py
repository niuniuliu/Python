class Parent(object):
	
	def alter(self):
		print "Parent alter()"
	def __init__(self, where):
		print "Parent __init__, i'm in ", where

class Child(Parent):

	def alter(self):
		print "Child. Before Parent alter"
		super(Child, self).alter()
		print "Child After Parent alter"
	def __init__(self, name):
		print "Child __init__, hello ", name
		super(Child, self).__init__('bj')


son = Child('TL')
# dad = Parent()


# dad.alter()
# son.alter()