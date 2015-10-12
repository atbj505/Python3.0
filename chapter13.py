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
