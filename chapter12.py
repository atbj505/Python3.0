#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程

class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s: %s' % (self.name, self.score))
	def get_grade(self):
		if self.score >= 90:
			print('A')
		elif self.score >= 60:
			print('B')
		else:
			print('C')

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
robert = Student('Robert Yang', 99)
robert.get_grade()
robert.age = 25
print(robert.age)

#访问限制
#通过在属性前添加__或_可以实现私有属性

class Student_new(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def printScore(self):
		print('%s: %s' % (self.__name, self.__score))
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_name(self, name):
		self.__name = name
	def set_score(self, score):
		self.__score = score
		
Jim = Student_new('Jim White', 75)
#print(Jim.__name)
print(Jim.get_name())
print(Jim.get_score())

#继承和多态

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Dog is eating...')

class Husky(Dog):
	pass

class Cat(Animal):
	def run(self):
		print('Cat is running...')
	def eat(self):
		print('Cat is eating...')
		
dog = Dog()
dog.run()
cat = Cat()
cat.run()

#获取对象信息

print(type(123))
print(type('123'))
print(type(None))
print(type(True))
print(type(abs))
print(type(dog))

print(type(123) == int)
print(type('123') == str)

import types
def fn():
	pass
	
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x : x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Husky))

#也可以判断变量的类型是不是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

#dir() 获取一个对象的所有属性和方法
print(dir('ABC'))

#__len__ 和len()等价
print(len('ABC'))
print('ABC'.__len__())

#getattr(), setattr(), hasattr()
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
		
obj = MyObject()
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))

print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())

#实例属性和类属性

class Student(object):
	name = 'Student'
	def __init__(self, name):
		self.name = name
		
s = Student('Bob')

print(s.name)
print(Student.name)
del s.name
print(s.name)
print(Student.name)