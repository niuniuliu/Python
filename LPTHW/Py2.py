# -*- coding=utf-8 -*-
#！/usr/bin/env python
import Py1

def test():
	print 'Py2 __name__ = ', __name__

if __name__ == '__main__':
	test()

print 'Py1.py __name__ = ', Py1.__name__

# 执行结果：
# __name__=__main__
# Py1.py __name__=Py1