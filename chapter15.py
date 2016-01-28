# /usr/bin/env python3
# -*- coding: utf-8 -*-

#IO编程

#文件读写

#方法一 直接读

#f = open('/Users/yangqihui/Desktop/Untitled-1.txt', 'r') #r表示读文字
#print(f.read())


#方法二 判断open结果
#try:
#    f = open('/Users/yangqihui/Desktop/Untitled-1.txt', 'r')
#    print(f.read())
#finally:
#    if f:
#        f.close()


#方法三 with语法省去close()操作
with open('/Users/yangqihui/Desktop/Untitled-1.txt', 'r') as f:
    print(f.read()) #全部读取
    print(f.read(10)) #读取10字节
    for line in f.readlines(): #按行返回list
        print(line.strip()) 


#二进制文件
f = open('/Users/yangqihui/Pictures/thumb.jpg', 'rb')
print(f.read())

#encoding 编码格式
#errors 遇到编码错误处理方式
f = open('/Users/yangqihui/gbk.txt', 'r', encoding = 'gbk', errors = 'ignore')


#写文件
#'w'写文本文件，'wb'写二进制文件

#f = open('/Users/yangqihui/gbk.txt', 'w')
#f.write('Hello, world!')
#f.close()
#
#with open('/Users/yangqihui/gbk.txt', 'w') as f:
#    f.write('Hello, world!')

#StringIO和BytesIO

from io import StringIO

#写入内存
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

#从内存读出
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#写入内存
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

#从内存读出
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())