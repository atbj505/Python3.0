#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高级特性

#切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])

print(L[:3])

print(L[-2:])

L = list(range(0,10))

print(L[:10:2])

print(L[::5])

print(L[-5:])

#拷贝，M=L同样效果
M = L[:]

N = L

L = [1 , 2, 3]

print(L)

print(M)

print(N)

O = tuple(range(0, 10))

P = O[:3]

print(P)

print('ABCDEF'[:3])

print('ABCDEF'[2:])

#迭代

print('========迭代')

d = {'a':1, 'b':2, 'c':3, 'd':4}
for key in d.keys():
	print(key)
for value in d.values():
	print(value)
for (key, value) in d.items():
	print(key, value)
	
for ch in 'ABC':
	print(ch)
	
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

#列表生成式

print('========列表生成式')

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

import os

print([d for d in os.listdir('/Users/yangqihui')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }

print([key + '=' + value for key, value in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']

print([l.lower() for l in L])