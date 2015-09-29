#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数

#调用函数

#abs 绝对值
print(abs(100))

print(abs(-20))

#max 最大值
print(max(1,2,3,4,5))

#类型转换
print(int('123'))

print(int(12.34))

print(str(123))

print(bool(1))

print(hex(123))

print(hex(255))


#定义函数

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0: 
		return x
	else:
		return -x

print(my_abs(10))
print(my_abs(-10))

#空函数

def nop():
	pass
	
#返回多个值

import math

def	move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
	
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

r = move(100, 100, 60, math.pi / 6)
print(r)



#函数的参数

#默认参数必须指向不变对象，如果指向可变对象则需要 = None来实现

def	power(x, n = 2):
	temp = 1
	while n > 0:
		n = n - 1
		temp = temp * x
	return temp

print(power(5))
print(power(5, 2))
print(power(6, 2))

#可变参数

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n * n
	return sum
	
print(calc(1,2,3))
print(calc())
num = [1, 2, 3]
print(calc(*num))
num2 = (1, 2, 3)
print(calc(*num2))

#关键字参数

def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
	
person('Michael', 30)
person('Bob', 35, city = 'beijing')
person('Adam', 45, gender = 'M', job = 'Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


#命名关键字参数

def person2(name, age, *, city, job):
	print(name, age, city, job)
person2('Jack', 24, city = 'Beijing', job = 'Engineer')