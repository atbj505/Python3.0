#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数式编程
#函数式编程的特点是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数

#高阶函数

#变量指向函数,函数名称可以看成一个变量 例如abs()的函数名abs就可以看作一个变量

f = abs
print(f)
print(f(-10))

#函数名也是变量
def add(x, y, f):
	return f(x) + f(y)
print(add(-10, 10, abs))

#map/reduce

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
	return x * x
r = map(f, [1, 2, 3, 4, 5])
print(r)
print(list(r))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#其中f必须有两个形参

from functools import reduce
def add_1(x, y):
	return x + y
result = reduce(add_1, [1, 2, 3, 4, 5])
print(result)

print(sum([1,2,3,4,5]))

def fn(x, y):
	return x * 10 + y
	
result = reduce(fn, [1, 2, 3, 4, 5])
print(result)

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

result = reduce(fn, map(char2num, '12345'))
print(result)

#lambda匿名函数

def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, '12345'))
result = str2int('12345')
print(result)

#练习

def fn_1(name):
	return name[0].upper()+name[1:].lower()
	
L1 = ['adam', 'LISA', 'barT']
print(list(map(fn_1, L1)))

def fn_2(L):
	def subFn(x, y):
		return x * y
	return reduce(subFn, L)

print(fn_2([1, 2, 3, 4]))

def fn_3(s):
	str1, str2 = s.split('.')
	def subFn(x, y):
		return x * 10 + y
	return reduce(subFn, map(int, str1)) + reduce(subFn, map(int, str2)) / 10 ** len(str2)

print(fn_3('123.45'))

def fn_4(x, y):
	return x * x + y * y
print(reduce(fn_4, [1, 2, 3]))
print(reduce(lambda x, y : x * x + y * y, [1, 2, 3]))

#filter
#filter用于过滤序列,filter()也接收一个函数和一个序列,filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
	return n % 2 == 1
print(filter(is_odd, [1, 2, 3, 4, 5, 6]))
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', 'B', None])))

print('=============')

def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n
		
def _not_divisible(n):
	def fun(x):
		return x % n > 0
	return fun
	
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it) #此处虽然传递了参数n但是返回的还是函数名称
		
for n in primes():
	if n < 100:
		print(n)
	else:
		break
		
#练习-回数

def is_palindrome(n):
	s = str(n)
	s1 = s[::-1]
	return s == s1
output = filter(is_palindrome, range(1, 1000))
print(list(output))

#sort

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key = abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))

#练习

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0].lower()
def by_score(t):
	return t[1]
	
L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score)
print(L3)