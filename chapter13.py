#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象高级编程

class Student(object):
	pass
	
s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

#但是给一个实例绑定方法，对另一个实例是不起作用的

s2 = Student()
#s2.set_age(25)

#可以给class绑定方法
def set_score(self, score):
	self.score = score
Student.set_score = MethodType(set_score, Student)
s.set_score(100)
print(s.score)
s2.set_score(90)
print(s2.score)

#使用__slots__可以限制属性

class Student_slots(object):
	__slots__ = ('name', 'age')

s = Student_slots()
s.name = 'Michael'
s.age = 25
#s.score = 99

class GraduateStudent(Student_slots):
	pass
g = GraduateStudent()
g.score = 99

#__slots__的限定对于子类无效，子类需要重新设定__slots__

#使用@property

class Student_property:
	def __init__(self):
		pass
	#score的get方法
	@property
	def score(self):
		return self._score
	#score的set方法
	@score.setter
	def score(self, score):
		if not isinstance(score, int):
			raise ValueError('score must be integer!')
		elif score < 0 or score > 100:
			raise ValueError('score must between 1-100!')
		self._score = score
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def brtth(self, birth):
		self._birth = birth
	
	#age的get方法	
	#age只有get方法，所以age为只读属性
	@property
	def age(self):
		return 2015 - self.birth
		
s = Student_property()
s.score = 60
print(s.score)
#s.score = 999
#s.age = 25

#练习
class Screen:
	def __init__(self):
		pass
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, width):
		self._width = width
	
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, height):
		self._height = height
		
	@property
	def resolution(self):
		return self._width * self._height
		
screen = Screen()
screen.width = 10;
screen.height = 20;
print(screen.width, screen.height)
print(screen.resolution)

#多重继承

class Animal(object):
	pass
class Mammal(Animal):
	pass
class Bird(Animal):
	pass
class Parrot(Mammal):
	pass
class Ostrich(Bird):
	pass
class RunnableMixIn(object):
	def run(self):
		print('Running')
class FlyableMixIn(object):
	def fly(self):
		print('Flying')
class CarnivorousMixIn(object):
	pass
class HerbivoresMixIn(object):
	pass

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
	pass

#定制类

#__str和__repr__用于打印类对象信息
class Student_str(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student_str object (name:%s)' % self.name

s = Student_str('Bob')
print(s)

#__iter__方法返回一个迭代对象
#__next__方法实现迭代规则
#__getitem__返回下标元素
#__setitem__元素赋值
#__delitem__删除元素
class Fib(object):
	def __init__(self):
		self._a, self._b = 0, 1
	def __iter__(self): #返回迭代对象
		return self
	def __next__(self): #设置迭代规则
		self._a, self._b = self._b, self._a + self._b
		if self._a > 100:
			raise StopIteration();
		return self._a
	def __getitem__(self, n):
		if isinstance(n, int): #指定下标的情况
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice): #切片的情况
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
			
for n in Fib():
	print(n)
f = Fib()
print(f[0], f[1], f[2], f[3], f[4])
print(f[:5])

#__getattr__当属性不存在时设置返回信息
class student_getattr(object):
	def __init__(self):
		self.name = 'Michael'
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda: 25
		raise AttributeError("'Student' object has no attribute '%s'" % attr)
s = student_getattr()
print(s.name)
print(s.score)
print(s.age)
print(s.age())
#print(s.abc)

#__getattr__应用场景 链式调用
#__call__对实例进行调用 相当于重载了对象的()运算符
class chain(object):
	def __init__(self, path = ''):
		self._path = path
	def __getattr__(self, attr):
		#if attr == 'user':
		#	return lambda x :chain('%s/%s' % (self._path, x))
		return chain('%s/%s' % (self._path, attr))
	def __call__(self, attr):
		return chain('%s/%s' % (self._path, attr))
	def __str__(self):
		return self._path
	__repr__ = __str__
	
print(chain().usr.bin.env.python)
print(chain().github.user('atbj505').repo)

#callable 判断对象是否能被调用
print(callable(chain()))
print(callable(max))
print(callable([1, 2, 3]))
print(callable('str'))

#枚举类

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)


from enum import Enum, unique
@unique #保证没有重复值
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

print(Weekday.Mon)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday(1))

day1 = Weekday.Mon
print(day1 == Weekday.Mon)
print(day1 == Weekday(1))
print(day1 == Weekday.Sun)

#元类

#type()
class Hello(object):
	def hello(self, name = 'world'):
		print('Hello, %s' % name)
		
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

#创建class的方法是使用type()函数实现的
#type()传入3个参数
#1.类名
#2.继承的父类集合(元组)
#3.class的方法名与函数绑定
def fn(self, name = 'Fuck'):
	print('%s, world.' % name)
World = type('World', (object,), dict(world = fn))

w = World()
w.world()
print(type(World))
print(type(w))

#metaclass 创建class