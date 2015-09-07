# # coding = utf-8

# def f(x):
#     return x * x

# # print map(f, [1,2,3,4,5])
# # print map(f, (1,2,3))

# a_list = []
# for i in xrange(26):
#     a_list.append(chr(i+ord('A')))

# # print a_list    


# def add(x, y):
#     return x + y

# # print reduce(add, [1,2,3,4,5])

# def fn(x, y):
#     return x * 10 + y

# # print reduce(fn, [1,3,5,7,9])

# def char2num(s):
#     return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

# # print char2num('1')

# # print map(char2num, '13579')



# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y

#     def char2num(s):
#         return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

#     # return reduce(fn, map(char2num, s))
#     return reduce(lambda x, y: x * 10 + y , map(char2num, s))


# # print str2int('1232132121312321')


# def capfirstchar(s):
#     return s[0].upper() + s[1:].lower()
# s_input = ['adam', 'LISA', 'barT']
# # s_input2 = ['adam', 'LISA', 'barT']

# # print map(capfirstchar, s_input, s_input2)

# i_list = [1,2,3,4,5]

# def multiple(i_list):
#     return reduce(lambda x, y: x * y, i_list)


# # print multiple(i_list)

# lst_a = [1,2,3]
# lst_b = [4,5,6]

# lst_new = [x * y for x in lst_a for y in lst_b ]
# # print map(lambda x, y: x * y, lst_a, lst_b)
# # print map(lambda x, y: (x * y, x + y), lst_a, lst_b)
# # print map(None, lst_a, lst_b)
# # print zip(lst_a, lst_b)

# n = 5
# # print reduce(lambda x, y: x * y, range(1, n + 1))


# def isPrime(num):
#     for i in range(2, 101):
#         if num % i == 0:
#             return False
#         return True

# def isNotPrime(num):
#     for i in range(2, 101):
#         if num % i == 0:
#             return True
#         return False


# x = filter(isPrime, range(1, 101))
# y = filter(isNotPrime, range(1, 101))

# # print y


# # lambda x: x% == 0 for x in range(1, 101)

# # print int('12345', base=8)
# # print float('123.5')
# def int2(x, base=2):
#     return int(x, base)

# # print int2('1010101')

# def getlist(*x):
#     ls = []
#     for i in x:
#         ls.append(i)
#     return ls

# import functools

# getl = functools.partial(getlist, 1,2,3)
# # print getl(4,5,6)

# max2 = functools.partial(max, 100, 10, 20)

# # print max2(5,6,7)


# class Card(object):

#     def __init__(self,name,Na,Lv,Ra,ATK,DEF):
#         self.name=name
#         self.Na=Na
#         self.Lv=Lv
#         self.Ra=Ra
#         self.ATK=ATK
#         self.DEF=DEF
    
#     def print_card(self):
#         print '%s:%s,%s,%s,%s,%s' % (self.name, self.Na, 
#             self.Lv, self.Ra, self.ATK, self.DEF)

# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# # std = Student('tl', 90)        
# card = Card('Dark Armed Dragon','Darkness',7,'Dragon',2800,1000)

# # card.print_card()



# # for i in dir(calendar):
# #     print i


# # import calendar

# # for i in range(1, 13):
# #     print calendar.month(2015, i)





# class Animal(object):
#     def run(self):
#         print "Animal is running"

# def run_twice(x):
#     x.run()
#     x.run()

# class ab(object):
#     def run(self):
#         print 'ab is run'

# # run_twice(ab())

# #result:
# # ab is run
# # ab is run

# # print dir(Animal().run)


# from types import MethodType
# print help(MethodType)

# class Student(object):
#     pass

# def set_age(self, age):
#     self.age = age

# Student.set_age = MethodType(set_age, Student)
# a = Student()
# a.set_age(10)
# print a.age


# class Student_1(object):
#     pass

# instance = Student_1()
# instance.set_age = MethodType(set_age, instance)
# instance.set_age(100)
# print instance.age




# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#     __repr__ = __str__

# # print Student('T.L')
# # s = Student('TimLiu')
# # print s


# # class say_hi():
# #     def __init__(self):
# #         print 'h'



# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1

#     def __iter__(self):
#         return self

#     def next(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 1000:
#             raise StopIteration();
#             # raise say_hi()
#         return self.a
    
#     def __getitem__(self, n):
        
#         if isinstance(n, int):
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a

#         if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             # print start
#             # print stop
#             a, b = 1, 1
#             L = []

#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b

#             return L


# f = Fib()
# print f[:10:2]
# a = [1,2,3,4,5]



# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'

#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 99
#             # return lambda:99
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# s = Student()
# print s.name
# print s.score1

# class Chain(object):

#     def __init__(self, path = ''):
#         self._path = path

#     def __getattr__(self, path):
#         # if hasattr(path, '__call__'):
#         #     path = ':' + path.__name__
#         return Chain('%s/%s' %(self._path, path))

#     def __str__(self):
#         return self._path

# print Chain().user.repos


# class Chain(object):

#     def __init__(self, attr = ''):
#         self._attr = attr
    
#     def __getattr__(self, attr):
#         return Chain('%s/%s' %(self._attr, attr))

#     def __str__(self):
#         return self._attr

#     def __call__(self, argv0 = ''):
#         return Chain('%s/:%s' %(self._attr, argv0))

# print Chain().user('Michael').repos.a1.a2.a3


# print dir(slice)

# class Student(object):
#     def __init__(self, name):
#         self.name = name

#     def __call__(self, age = 10):
#         print (self.name, age)

# Student('TL')('11')

