# /usr/bin/env python3
# -*- coding: utf-8 -*-

#操作文件和目录

import os

print(os.name) #posix说明是linux，unix，max os。nt是windows
#详细的系统信息
print(os.uname())
#环境变量
print(os.environ)
print(os.environ.get('PATH'))
#查看当前目录的绝对路径
print(os.path.abspath('.'))
#生成完整路径并表示出来
#将两个路径合成一个时，不要直接拼字符串，而是通过os.path.join(),这样可以区分不同操作系统的路径分隔符
print(os.path.join('/Users/yangqihui', 'testdir'))
#创建文件夹
os.mkdir('/Users/yangqihui/testdir')
#删除文件夹
os.rmdir('/Users/yangqihui/testdir')
#拆分文件路径
print(os.path.split('/Users/yangqihui/testdir/file.txt'))
#获取扩展名
print(os.path.splitext('/Users/yangqihui/testdir/file.txt'))
#文件重命名
#os.rename('test.txt', 'text.py')
#删除文件
#os.remove('test.py')
#列出所有文件夹
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] =='.py'])