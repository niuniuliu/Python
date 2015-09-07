# -*-coding=utf-8-*-

# a_set = set([1,2,3,4])
# b_set = set(['a', 'b', 'c'])
# c_set = set([(1,2,3), (4, 5, 6)])
# print a_set, b_set, '\r'
# print len(a_set)
# print len(b_set)
# print len(c_set)
# print c_set
# print type(a_set)

# a_dict = {(1,2,3):'123', ([1,(2,3)]): '1(23)', (1, [2,3]): '1[23]'} # issue line
# b_dict = {(1,2,3):'123', (1,(2,3)): '1(23)'}
# print b_dict
# print b_dict.items()




# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x > 0:
#         return x
#     else:
#         return -x

# print my_abs(1)
# print  my_abs('x')




# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)
# print x, y
# x, y = move(100, 100, 6, math.pi / 6)
# print x, y




# def power(x, n = 2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# print power(100, 3)
# print power(100)




# def enroll(name, gender, age=6, city='Beijing'):
#     print 'name:', name
#     print 'gender:', gender
#     print 'age:', age
#     print 'city:', city

# enroll('Bob', 'M', 7)
# print 
# enroll('Adam', 'M', city='Tianjin')

# enroll('Adam', 'M', 'Tianjin') # age = 'Tianjing' python don't soo smart to judge by data type




# def add_end(L=[]):
#     L.append('END')
#     return L

# print add_end()
# print add_end()
# print add_end()

# # change to 
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print add_end()
# print add_end()
# print add_end()



# def calculate(numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i * i 
#     return sum

# print calculate([1,2,3,4,5,6])

# def calculate(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i * i 
#     return sum
# print calculate(1,2,3,4,5,6)

# a = (1,2,3,4,5,6)
# a2 = [1,2,3,4,5,6]

# print calculate(*a)
# print calculate(*a2)
# print calculate(*[])





# def func(a, b, c=0, *args, **kw):
#     print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
# func('a', 'b', 'c', 'd', 'e', 'f', x=8)

# def func1(x, y, z=[11], *args, **key_value):
#     print 'x: ', x, '\r'
#     print 'y: ', y, '\r'
#     print 'z: ', z, '\r'
#     print 'args: ', args,'\r'
#     print 'key_value: ', key_value,'\r'

# func1(1, 2, 3, 'a', 'b', 'c', a=99)
# func1([11, 11], 'b', 'c', 'd', 'e', 'f', ee=True, es = False)
# func1([11, 11], 2, ee=True, es = False)
# func1([11, 11], 'b', *('d', 'e','f'), **{'a' : True, 'b': False})
# func1([11, 11], 'y', *('1', '2','3'), **{'a' : True, 'b': False})
# func1("x", "y", z = 1, **{'a': 1})
# func1("x", "y", '\"z\"', *(4,5,6), a = 1)




# def func1(x='x', y='y', z='z', *args): #, **kw):
#     print 'x: ' + x
#     print 'y: ' + y
#     print 'z: ' + z
#     print '*args: ' + str(args)
    # print '**kw: ' + str(kw)

# func1(x='x1')
# func1(x = "x", y = "y", z = 'z', 1, w=1)
# func1("x", "y", 'z', *(1,2,3,4))


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)




# from tail_call_optimized import tail_call_optimized

# def fact(n):
#     return fact_iter(1, 1, n)

# @tail_call_optimized
# def fact_iter(product, count, max):
#     if count > max:
#         return product
#     return fact_iter(product * count, count + 1, max)

# print fact(1000)




# print ['1','2',3,4,5][0:3:1]




# from collections import Iterable
# print isinstance('12', Iterable)

# for i, value in enumerate(["a", 'b', 'c', 'd']): #enumerate([x for x in range(10)]):
#     print i, value

# print [x for x in range(10)]

# for x, y in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']):
#     print x, y

# list_tuple = [("x", 'a'), ("x", 'b'), ("x", 'c'), ("x", 'd'), ("x", 'e'), ("x", 'f'), ("x", 'g'), ("x", 'h')]
# for x, y in list_tuple:
#     print x, y 




# a = [x + str(i) for x in 'ABC' for i in range(4)]
# # print a

# import os
# # print [d for d in os.listdir('.')]

# L = ['Hello', 'World', 18, 'Apple', None]

# print [s.lower() for s in L if isinstance(s, str)]


# L = ['Hello', 'World', 18, 'Apple', None]
# l = [s.lower() for s in L if isinstance(s, str)]
# t_tuple = (i for i in l)
# # print type(t_tuple)
# print t_tuple

# for x in t_tuple:
#     print x

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print b
#         a, b = b, a + b
#         n = n + 1

# fib(6)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1

# print fib(6)

# for x in fib(6):
#     print x

# def fib(x):
#     while x < 10:
#         yield x
#         x += 1

# print [i for i in fib(1)]

# from collections import Iterable
# print isinstance(fib(1), Iterable)





# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax

# # print calc_sum(1,2,3,4)

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum

# f1 = lazy_sum(1,2,3,4)
# f2 = lazy_sum(1,2,3,4,5)
# print f1()
# print f2()

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f(j):
#             def e():
#                 # pass
#                 return j*j
#             return e

#         fs.append(f(i))
#     return fs

# f1, f2, f3 = count()

# print f1, f2, f3
# print f1(), f2(), f3()

# def x():
#     fs = []
#     for i in range(1, 4):
#         def y(i):
#             def z():
#                 return i*i
#             return z
#         fs.append(y(i))

#     return fs

# # print x()
# f1, f2, f3 = x()
# print f1(), f2(), f3()






def x():
    fs = []
    for i in range(1, 4):
        fs.append(lambda i: i*i)
    return fs

# print x()
# f1, f2, f3 = x()
# print f1(), f2(), f3()

def build(x, y):
    return lambda: x*x + y*y

# print (lambda x, y: x*x + y*y)(1, 12)
# x =build(1, 2)
# print x()

f = lambda x: x*x
# print f(5)
# print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def build1(x, y):
    return lambda: x*x + y*y

def build2(x, y):
    return lambda x, y: x*x + y*y

# print build1(1,411111)()
# print build2(1,411111)(1,2)

# def up_level():  
#     var1 = 30  
#     def in_level ():  
#         return var1
#     return in_level()  

# print up_level()


# x = 10
# def foo():
#     y = 5
#     bar = lambda : x + y
#     print bar()
#     y =15
#     print bar()
    
# foo()

# x = 10
# def foo():
#     y = 5
#     bar = lambda y=y: x + y
#     print bar()
#     y =15
#     print bar()
    
# # foo()

# # y = 5
# y = 15
# z1 = lambda x = x: x + y
# y = 1500
# # print z1()



# # g = lambda x,y,z:x+y+z
# z = 1
# xg = lambda:z+z
# def xg1():
#     return z
# # print xg()
# # print xg1()


# g = lambda x,y,z:x+y+z
# g1 = lambda :x+y+z
# print g1()

# @getdata2
# 可以忽略x,y，我的理解是，忽略之后作用域发生了改变。
# g=lambda: x*x+y*y 也就是
# def explore_lambda():
#     return x*x + y*y
# x,y不再是传入的参数，而是函数外部的变量。
# ==========
# 而g=lambda x,y: x*x+y*y，相当于
# def explore_lambda(x, y):
#     return x*x + y*y
# 此时，x，y是函数传入的参数

# ==========
# def build(x,y): 
#     return lambda:x*x+y*y 这里的x, y并非是lambda函数的参数，而是build()函数传入的。
# 所以调用的时候是 build(x, y)()

# 请问，@廖雪峰，我的理解对么




# def now():
#     print '2014-12-29'

# f = now
# print f.__name__
# f()

# def log(func):
#     def wrapper(*args, **kw):
#         print "call %s(): " %func.__name__
#         return func(*args, **kw)
#     return wrapper


# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print "%s %s(): " %(text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# import functools

# def log(text = None):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             # print text
#             print "%s %s(): " %(text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log('execute')
# def now():
#     print '2014-12-29'
# now()


# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         # print text
#         print "Begin Call %s(): " %(func.__name__)
#         func(*args, **kw)
#         print "End Call %s(): " %(func.__name__)
#     return wrapper

# @log
# def now():
#     print '2014-12-29'

# # now = log('execute')(now)
# # now = log(now)
# # print now.__name__
# now()


# import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         # print text
#         print "Begin Call %s(): " %(func.__name__)
#         func(*args, **kw)
#         print "End Call %s(): " %(func.__name__)
#     return wrapper

# @log
# def now():
#     print '2014-12-29'

# # now = log('execute')(now)
# # now = log(now)
# # print now.__name__
# now()


# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# import functools

# def log(arg):
#     if hasattr(arg, '__call__'):
#         @functools.wraps(arg)
#         def wrapper(*args, **kw):
#             print 'call %s():' % arg.__name__
#             return arg(*args, **kw)
#         return wrapper
        
#     def decorate(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print '%s %s()' % (arg, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorate

    
# @log('excute')
# def now():
#     print '2014-08-12'
# now()

# @log
# def now():
#     print '2014-08-12'
# now()

# import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print 'begin call'
#         result = func(*args, **kw)
#         print 'end call'
#         return result
#     return wrapper
      
# # @log
# def now():
#     print '2014-08-12'
  
# now = log(now)
# # print now.__name__
# now()

# def log(string): 
#     if  isinstance(string,str):
#         def decorator(func):
#             def wrapper(*args,**kw):
#                 print '%s %s' %(string,func.__name__)
#                 return func(*args,**kw)
#             return wrapper
#         return decorator
#     else:
#         def wrapper(*args,**kw):
#             print '%s' %string.__name__
#             return string(*args,**kw)
#         return wrapper

# @log
# def f1():
#     pass


# @log('excute')
# def f2():
#     pass

# f1()
# f2()


# 无参数装饰器 – 包装无参数函数
# def decorator(func):
#     print "this is: begin [" + func.__name__ + ']'
#     x = func
#     print "this is: end [" + func.__name__ + ']'
#     return x

import functools

def decorator(func):
    @functools.wraps(func)
    def wrap(*args, **kw):
        print "this is: begin [" + func.__name__ + ']'
        x = func(*args, **kw)
        print "this is: end [" + func.__name__ + ']'
        return x
    return wrap

@decorator
def foo():
    print 'Hello foo'

# print foo.__name__
# foo()

def log(text):
    def newDecorator(func):
        @functools.wraps(func)
        def wrapper(*x, **y):
            print 'begin %s: %s' % (text, func.__name__)
            x = func(*x, **y)
            print 'end %s: %s' % (text, func.__name__)
            # print '===>' 
            # print text
            # print func
            # print x
            # print y
            # print  '<==='
            return x
        return wrapper
    return newDecorator

x = {'name': 'TL', 'gender': 'male'}

# @log
# def getKey_TL(dict):
#     key_list = []
#     for key in dict:
#         key_list.append(key)
#     print key_list
#     return key_list

# getKey_TL = log('text')(getKey_TL)
# getKey_TL(x)



def getKey_TL(args):
    # if args:
    #     argument = args[0]
    # elif dict:
    #     argument = dict
    
    key_list = []
    for key in args:
        key_list.append(key)
    print key_list
    return key_list

# getKey_TL = log('text')(getKey_TL)
# getKey_TL(x = 1, y = 2, z= 3, a = 4)
# getKey_TL(x)
# getKey_TL(1,2,3,4)



# def decorator_whith_params_and_func_args(arg_of_decorator):
#     def handle_func(func):
#         def handle_args(*args, **kwargs):
#             print "begin"
#             func(*args, **kwargs)
#             print "end"
#             print arg_of_decorator, func, args,kwargs
#         return handle_args
#     return handle_func


# @decorator_whith_params_and_func_args("1234")
# def foo4(a, b=2, c=3):
#     print "Content"

# foo4(1, b=3, c= 5)

# class A():

#     @staticmethod
#     def test_static():
#         print "static"
#     @classmethod
#     def test_class(cls):
#         print "class", cls

#     def test_normal(self):
#         print "normal"

#     def test_normal_method(x):
#         print "normal1"

# a = A()
# # A.test_static()
# # A.test_normal()
# # A.test_normal_method()
# # A.test_class()
# # a.test_static()
# # a.test_normal()
# # a.test_class()
# # a.test_normal_method()

# def printDict(**dict_):
#     for x in dict_.items():
#         print x

# # printDict(**globals())
# # print __file__

# # print globals()

# # CONST PI = 1
# PI = 2
# print PI



# a_file = r"C:\Users\tliu\Documents\APDS\AdventPortfolioDataServices\Archive\2015_Jan\history.txt"

# file_content = open(a_file, 'r')
# # print type(file_content)

# # for x in file_content.readlines():
# #     print x

# x = file_content.readlines()

# print len(x)

# print len(set(x))

# y = list(set(x))


# file_content.close()

# for i in y:
#     print i,

# print ord('a')
# print ord('A')
# print chr(97)
# print chr(65)

str_cn = '中文'

print len(str_cn)
print type(str_cn)

# print r'中文'

print r'中文'

