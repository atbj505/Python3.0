#!/usr/bin/python
#python 缩进格式
a = 100
if a >=0:
	print('a = ' , a)
else:
	print('a = ' , -a)

#\转义字符
print('i\'m ok')
print("i'm ok")
print('i\'m \\ok')

#r''不转义
print(r'\\\\r\\\\')

#''' '''表示多行类似于\n
print('''line1
line2
line3''')

#布尔值
print('3>2',3>2)
print('2>3',2>3)

print('3>2 and 2>3',3>2 and 2>3)
print('3>2 or 2>3',3>2 or 2>3)

print(not True)
print(not False)

#空值None
print('None',None)

#变量
a = 'abc'	#a指向abc
b = a		#b指向abc
a = 'xyz'	#a指向xyz
print('a',a)
print('b',b)

#常量 大写表示常量
PI = 3.1415
print('PI',PI)

#除法
print(10/3.0)
print(10//3.0)

#练习
n=123
print("n =",n)
f = 456.789
print('f =',f)
print('s1 =','\'Hello, world\'')
print('s2 =','\'Hello, \\\'Adam\\\'\'')
print('s3 =',r'Hello, "Bart"')
print('s4 =',r'Hello')
print('Lisa!\'\'\'')