#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#返回函数

def calc_sum(*args):
	ax = 0
	for n in args:
		ax += n
	return ax
l = [1, 2, 3]
print(calc_sum(*l))

def lazy_sum(*args):
	def sum():
		ax = 0;
		for n in args:
			ax += n
		return ax
	return sum
	
f = lazy_sum(*l)
print(f)
#f()被称为闭包
print(f())

#即使参数相同，闭包也不同
f1 = lazy_sum(*(1, 2, 3))
f2 = lazy_sum(*(1, 2, 3))
print(f1 == f2)

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs
	
f1, f2, f3 = count()
print(f1(), f2(), f3())

#f1(), f2(), f3()返回的都是9 问题在于原因就在于返回的函数引用了变量i，而i此时等于3

#解决的方案是

def count_1():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs

f1, f2, f3 = count_1()
print(f1(), f2(), f3())

#匿名函数

print(list(map(lambda x : x * x, [1, 2, 3])))

f = lambda x : x * x
print(f)
print(f(5))

#匿名函数作为返回值
def build(x, y):
	return lambda x, y: x * x + y * y
	

#装饰器

def now():
	print('2015-3-25')
f = now
f()
print(now.__name__)
print(f.__name__)

#decorator

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
@log #相当于执行了 now_1 = log(now_1)
def now_1():
	print('2015-3-25')

now_1()

#能传参的decorator

def log_1(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log_1('execute') #相当于执行了now_2 = log('excute')(now_2)
def now_2():
	print('2015-3-25')
now_2()
print(now_2.__name__) #函数名称变了 可以通过functools.wraps改变函数名称

import functools

def log_2(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
	
@log_2('excute')
def now_3():
	print('2015-3-25')

now_3()
print(now_3.__name__)

#练习

def logTest(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('begin %s %s' % (text, func.__name__))
			func(*args, **kw)
			print('end %s %s' % (text, func.__name__))
		return wrapper
	return decorator
	
@logTest('test')
def now_4():
	print('2015-3-25')
	
now_4()

#偏函数

print(int('12345'))

print(int('12345', base = 8))

print(int('12345', 8))

def int2(x, base = 2):
	return int (x, base)
	
print(int('100010', base = 2))

print(int2('100010'))

#用偏函数实现

import functools

int2 = functools.partial(int, base = 2)

print(int2('100010'))