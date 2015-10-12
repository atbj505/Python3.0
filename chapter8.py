#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#生成器

L = [x * x for x in range(1, 11)]

print(L)

P = (x * x for x in range(1, 11))

print(P)

print(next(P))
print(next(P))
print(next(P))
print(next(P))

g = (x * x for x in range(10))
for n in g:
	print(n)

#yield关键字
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'
	
def fib1(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

fib(6)
f = fib1(6)
print(f)

for n in fib1(6):
	print(n)
	
#获取fib1 return的返回值

while True:
	try:
		x = next(f)
		print('f:',x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
		
#杨辉三角练习

def triangles(count):
		l = [1]
		n = 1
		while n <= count:
			yield l
			l.append(1)
			for m in range(len(l)-2, 0, -1):
				l[m] += l[m - 1]
			n = n + 1
			
for n in triangles(6):
	print(n)

#迭代器
from collections import Iterable
from collections import Iterator
print(isinstance((x for x in range(10)), Iterable))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterable))
print(isinstance([], Iterator))
print(isinstance({}, Iterable))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterable))
print(isinstance('abc', Iterator))

#[] {} 'abc'是可迭代对象，但是不是迭代器
#通过iter()方法可以转换成迭代器

print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('abc'), Iterator))

#凡是可作用于for循环的对象都是Iterable对象
#凡是可作用于next()方法的对象都是Iterator类型