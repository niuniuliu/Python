def fn(a, b, c=0, *args, **kw):
    print 'a =', a, ', b =', b, ', c =', c, ', args =', args, ', kw =', kw

# print '\n==> fn(1, 2)'
# fn(1, 2)
# print '\n==> fn(1, 2, 3)'
# fn(1, 2, 3)
# print '\n==> fn(1, 2, 3, 4)'
# fn(1, 2, 3, 4)
# print '\n==> fn(1, 2, k1=8, k2=9)'
# fn(1, 2, k1=8, k2=9)
# print '\n==> fn(1, 2, 3, k1=8, k2=9)'
# fn(1, 2, 3, k1=8, k2=9)
# print '\n==> fn(1, 2, 3, 4, k1=8, k2=9)'
# fn(1, 2, 3, 4, k1=8, k2=9)

# interesting part:
# print '\n==> fn(*(1, 2))'
# fn(*(1, 2))

# print '\n==> fn(*(1, 2, 3))'
# fn(*(1, 2, 3))

# print '\n==> fn(*(1, 2, 3, 4))'
# fn(*(1, 2, 3, 4))

# # TypeError: fn() takes at least 2 arguments (1 given)
# print '\n==> fn(*(1, ))'
# fn(*(1, ))
# fn(*((1, ), (2, )))

# print len('a1',  )