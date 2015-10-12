#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#字符串 编码
print(ord('a'))
print(ord('中'))

print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

x = 'ABC'		#str类型
print('x =',x)
y = b'ABC'		#bytes类型
print('y =',y)

#.encode() 编码形式 str->bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

#.decode() 反编码 bytes->str
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#len() 计算字符长度
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

#格式化
print('%d-%02d'%(2,1))
print('%.2f'%3)

#练习
s1 = 72
s2 = 85

r = (s2-s1)/s1 *100

print('%02.01f%%'%r)
