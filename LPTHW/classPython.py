# -*- coding = utf-8 -*-

# class className:
# 	pass
#
# class people:
# 	name = 'jack' # class attribute.
#
# 	def printName(self): # Define a method
# 		print " -- Print class method printName(self)."
# 		print self.name
#
# print ' - Print class object attribute.'
# print people.name
#
#
# p = people()
# print ' - Print instance p attribute'
# print p.name
#
# print ' - Print instance p method'
# print p.printName()
#

#
# class people:
#     name = 'Jack'
#     age = '21'
#
# p = people()
# print p.name, p.age
#


# class people:
#     __name = 'Jack'
#     __age = 21
#
#     def getName(self):
#         return self.__name
#
#     def getAge(self):
#         return  self.__age
#
# p = people()
# print p.getName(), p.getAge()
# p.sex = 'male'
#
# print dir(p)
# print dir(people)
# print people._people__age
# print people._people__name




# class people:
# 	name = 'Jack'

# 	# __init__() is built-in method, it will be invoked once instance it.
# 	def __init__(self, age): 
# 		self.age = age


# p = people(12)

# print p.name
# print p.age

# print dir(p)
# print dir(people)
# # print people.__init__(1)

# print people.name
# # print people.age 


# class people:
# 	country = 'China'

# print people.country
# p = people()
# print p.country

# p.country = "US"

# print p.country
# print people.country

# del p.country
# print p.country


# class people:
# 	country = 'China'

# 	@classmethod
# 	def getCountry(cls):
# 		return cls.country

# p = people()
# print p.getCountry()
# print people.getCountry()



# class people:
# 	country = 'China'

# 	@classmethod
# 	def getCountry(cls):
# 		return cls.country

# 	@classmethod
# 	def setCountry(cls, country):
# 		cls.country = country


# p = people()
# print p.getCountry()
# print people.getCountry()

# p.setCountry('US')
# print p.getCountry()
# print people.getCountry()

# print dir(people)
# print people.country


# class people:
# 	country = 'China'

# 	def getCountry(self):
# 		return self.country

# p = people()
# print p.country
# print p.getCountry()
# # print people.getCountry()

class people:
	country = "China"
	city = 'Beijing'

	# p = people()
	@staticmethod
	def getCountry():
		return people.country
		# return p.country

print people.getCountry()
p = people
print p.country
print p.getCountry()
print people.city
print p.city