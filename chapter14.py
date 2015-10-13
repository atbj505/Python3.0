# /usr/bin/env python3
# -*- coding: utf-8 -*-

#错误、调试和测试

#错误处理

#try

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:', e)
	except ValueError as e:
		print('ValueError:', e)
	except ZeroDivisionError as e:
		print('ZeroDivisionError:', e)
	else:
		print('no error!')
	finally:
		print('finally...')

#main()
#print('end')

#logging 记录错误的堆栈信息

import logging

def main_log():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

#main_log()
#print('end')

#抛出错误

def foo_raise(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value: %s' % s)
	return 10 / n
def bar_raise():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError')
		raise

#bar_raise()

#调试

#断言

def foo_assert(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n

def main_assert():
	foo_assert('0')

#main_assert()

#logging

import logging
#设置记录信息的级别 有debug， info， warning， error四个级别
logging.basicConfig(level = logging.INFO)

s = '0'
n = int(s)
#logging.info('n = %d' % n)
#print(10 / n)

#pdb断点调试
#使用n单步调试
#使用p查看变量
#使用c继续执行
#使用q结束调试

import pdb

s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)

#单元测试

#创建mydict.py 和 mydict_test.py两个文件
#测试类需要继承自unittest.TestCase
#测试方法名需要以test开头

#运行单元测试
#python3 -m unittest mydict_test

#setUp,tearDown
#每次测试方法调用都会执行这两个方法


#文档测试
#见mydict类顶部的注释
