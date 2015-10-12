#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#模块

#把很多函数分组，放在不同的文件中，在python中，一个.py文件就称为一个模块

#包用来处理模块名相同的情况，其中包中都会拥有一个__init__.py的文件

'a test module'

__author__ = 'Robert'

import sys

def test():
	args = sys.argv
	print(args)
	if(len(args)) == 1:
		print('Hello World!')
	elif len(args) == 2:
		print('Hello %s!' % args[1])
	else:
		print('Too many arguments!')
		
if __name__ == '__main__':
	test()
	
#作用域

#普通变量是公开的 如 abc x123 PI等
#类似__name__是特殊变量，可以直接引用，但是有特殊用途
#类似_xxx和__xxx这类变量是非公开的，不应该直接引用

def _private_1(name):
	return 'Hello, %s' % name
	
def _private_2(name):
	return 'Hi, %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)

#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

#安装第三方模块

#pip install Pillow

from PIL import Image

im = Image.open('/Users/yangqihui/Pictures/thumb.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('/Users/yangqihui/Pictures/thumbnail.jpg', 'JPEG')