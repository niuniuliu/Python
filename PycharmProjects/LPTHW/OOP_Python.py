# -*- coding=utf-8 -*-
# import fileinfo
# import gc
# filepath = r"C:\Users\tliu\Music\06 TALK 3.mp3"

# f = fileinfo.FileInfo(filepath)
# for i in dir(f):
#     # print type(i), i
#     pass

# def leakmem():
#     f1 = fileinfo.FileInfo(filepath)

# # for i in range(1000000):
# #     leakmem()

# # print f.__class__
# # print f.__doc__
# # print f
# # print type(f)


# mp3file = fileinfo.MP3FileInfo()
# # print mp3file

# mp3file['name'] = filepath
# # print mp3file

# fsock = open(filepath, "rb", 0)


# def stripnulls(data):
#     "strip whitespace and nulls"
#     return data.replace("\00", "").strip()






# global var
# var = 23

# def func_local():
#     var = 10
#     print var

# def func_global():
#     var = 12100

# # func_global()
# # func_local()

# class MethodTest:
#     count= 0
#     def addCount(self):
#         MethodTest.count += 1
#         print"I am an instance method, my count is " + str(MethodTest.count), self
    
#     @staticmethod
#     def staticMethodAdd():
#         MethodTest.count += 1
#         print "I am a static methond, my count is " + str(MethodTest.count)

#     @classmethod
#     def classMethodAdd(cls):
#         MethodTest.count += 1
#         print "I am a class method, my count is " + str(MethodTest.count), cls

# class SubClass(MethodTest):
#     pass

# # x = MethodTest()
# # x.addCount()
# # # MethodTest().addCount()
# # x.staticMethodAdd()
# # MethodTest.staticMethodAdd()
# # x.classMethodAdd()
# # MethodTest.classMethodAdd()
# # b = SubClass()    
# # b.addCount()
# # b.staticMethodAdd()
# # b.classMethodAdd()
# # MethodTest.staticMethodAdd()

# class PrivateTest:
#     __myownedata = 12
#     def __myownmethod(self):
#         print "can you see me?"
#     def sayhi(self):
#         print "say hi"

# class subPrivateTest(PrivateTest):
#     pass

# # subPrivateTest.__myownedata
# # print dir(subPrivateTest)
# # print subPrivateTest._PrivateTest__myownedata


# class A1(object):
#     def __init__(self):
#         print("in init")
    
#     def __new__(self):
#         print("in new")
# # A1()


# class A(object):
#     def __new__(cls):
#         Object = super(A,cls).__new__(cls)
#         print "in New"
#         return Object
    
#     def __init__(self):
#         print "in init"

# class B(A):
#     def __init__(self):
#         print "in B's init"
# # B()

# class P:
#     def __del__(self):
#         print"deleted"

# class S(P):
#     def __init__(self):
#         print 'initialized'

#     def __del__(self):
#         P.__del__(self)
#         print"child deleted"

# # a = S()




# class A:
#     def sayhi(self):
#         print'I am A hi'
# class B:
#     def sayhi(self):
#         print'I am B Hi'
# class C(A,B):
#     pass

# # c = C()
# # B.sayhi(c)

# class AddrBookEntry(object):
#     'addressbook entry class'
#     def __init__(self, nm, ph):
#         self.name= nm
#         self.phone= ph
#         print'Created instance for:', self.name

#     def updatePhone(self, newph):
#         self.phone = newph
#         print'Updated phone# for:', self.name

# class EmplAddrBookEntry(AddrBookEntry):
    
#     'EmployeeAddress Book Entry class'
#     def updateEmail(self, newem):
#         self.email= newem
#         print'Updated e-mail address for:', self.name

# # john = EmplAddrBookEntry('John Doe', '408-555-1212')
# # john = EmplAddrBookEntry('John Doe', '408-555-1212', '')
# # print john.name



# class AddrBookEntry(object):
#     'addressbook entry class'
#     def __init__(self, nm, ph):
#         self.name= nm
#         self.phone= ph
#         print 'Created instance for:', self.name
    
#     def updatePhone(self, newph):
#         self.phone = newph
#         print 'Updated phone# for:', self.name

# class EmplAddrBookEntry(AddrBookEntry):
#     'EmployeeAddress Book Entry class'
#     def __init__(self, nm, ph, id, em):
#         # AddrBookEntry.__init__(self, nm,ph)
#         self.empid= id
#         self.email= em
    
    
#     def updateEmail(self, newem):
#         self.email= newem
#         print 'Updated e-mail address for:', self.name

# john= EmplAddrBookEntry('John Doe', '408-555-1212', 42, 'john@spam.doe')
# print john.email
# print john.empid
# # print john.name
# # print john.phone


# class AddrBookEntry(object):
#     'addressbook entry class'
#     def __init__(self, nm, ph):
#         self.name= nm
#         self.phone= ph
#         print 'Created instance for:', self.name
    
#     def updatePhone(self, newph):
#         self.phone = newph
#         print 'Updated phone# for:', self.name

# class EmplAddrBookEntry(AddrBookEntry):
#     'EmployeeAddress Book Entry class'
#     def __init__(self, nm, ph, id, em):
#         AddrBookEntry.__init__(self, nm,ph)
#         self.empid= id
#         self.email= em

#     def updateEmail(self, newem):
#         self.email= newem
#         print 'Updated e-mail address for:', self.name

# john= EmplAddrBookEntry('John Doe', '408-555-1212', 42, 'john@spam.doe')

# print john.email
# print john.empid
# print john.name
# print john.phone


# class A: 
#     attr=1

# class B(A):
#     pass

# class C(A):
#     attr=2

# class D(B,C):
#     pass

# x=D()

# print x.attr



# class dirTest(object):
#     value='1'
#     def sayhi(self):
#         self.name='cat'
#         print"hi"

# print dir(dirTest)
# # ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'sayhi', 'value']

# issubclass(sub,sup):判断一个类是另一个类的子类或子孙类
# isinstance(obj1,obj2):在判定一个对象是否是另一个给定类的实例
# callable()是一个布尔函数，确定一个对象是否可以通过函数操作符(())来调用。如果函数可
# 调用便返回True，否则便是False.

# 模块inspect:
# inspect模块提供了一系列自省函数，它可以获取模块，类，方法，函数，traceback，帧对象，代码对象的信息。常用的方法getmembers，ismodule，getcallargs，isclass等，更多详细信息参见http://docs.python.org/library/inspect.html
# import inspect
# inspect.isbuiltin(abs)
# True
# inspect.ismodule(inspect)
# True


# class Classic: 
#     pass
# class Newstyle(object): 
#     pass
# print type(Classic)
# print type(Newstyle)

# class TypeTestClass:
#     pass

# TypeTestClass = type('TypeTestClass',(),{})

# print TypeTestClass
# print TypeTestClass()




# class PropertyTest(object):
#     def __setProperty(self,value):
#         self.__property = value
#         # print self.__property
#         print"setting property"

#     def __getProperty(self):
#         print"getting property"
#         return self.__property
    
#     def __delProperty(self):
#         print "del proerty"
#         del self.__property

#     TestProperty = property(fget = __getProperty, fset = __setProperty, fdel = __delProperty, doc = "propertytest")
#     # TestProperty = property(__getProperty, __setProperty, __delProperty, "propertytest")


# p = PropertyTest()
# p.TestProperty = 11
# p.TestProperty
# del p.TestProperty
# p.TestProperty = 12
# p.TestProperty



# class SlotTest(object):
#     __slots__ = ('name','age')

# s = SlotTest()
# s.name="carol"
# s.age="12"
# # s.score="64"

# print dir(s)
# # ['__class__','__delattr__', '__doc__', '__format__', '__getattribute__','__hash__', '__init__', '__module__', '__new__', '__reduce__','__reduce_ex__', '__repr__', '__setattr__', '__sizeof__','__slots__', '__str__', '__subclasshook__', 'age', 'name']


# class Test(object):
#     pass

# s1=Test()
# s1.score="65"
# print dir(s1)
# # ['__class__','__delattr__', '__dict__', '__doc__', '__format__','__getattribute__', '__hash__', '__init__', '__module__', '__new__','__reduce__', '__reduce_ex__', '__repr__', '__setattr__','__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'score']


# def class_creator(func):
#     class internal:
#         pass
#     setattr(internal, func.__name__, func)
#     return internal

# def alive(self):
#     print 'Hi,I am here'

# ChildClass = class_creator(alive)
# cc=ChildClass()
# cc.alive()

class a(object):
    def __init__(self, x, y):
        print "x and y: " + x, y

class a(object):
    def __init__(self, x):
        print "x: " + x

# a1 = a('a')
a2 = a('a', 'b')