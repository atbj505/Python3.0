#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#条件判断 循环

age = 3
if age >= 18:
	print('your age is',age)
	print('adult')
elif age >= 6:
	print('your age is',age)
	print('teenager')
else:
	print('your age is',age)
	print('kid')
	
s = '1990'
birth = int(s)
if birth < 1990:
	print('90前')
else:
	print('90后')



names = ['Michael','Bob','Tracy']
for name in names:
	print(name)
	
sum = 0
for x in range(0,101,1):
	sum += x
print(sum)

sum = 0
n = 0
while n < 101:
	sum	+= n
	n += 1
print(sum)

l = ['Bert', 'Lisa', 'Adam']
for name in l:
	print('Hello, %s !' % name)