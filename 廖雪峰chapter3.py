#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list 和 tuple 数组 元组

classmates = ['Michael','Bob','Tracy']
print('classmates =',classmates)

#len()获取元素个数
print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

#append 数组末尾添加元素
classmates.append('Adam')
print(classmates)

#insert 插入到指定位置
classmates.insert(1, 'Jack')
print(classmates)

#pop 删除末尾元素
classmates.pop()
print(classmates)

#pop()删除指定元素
classmates.pop(1)
print(classmates)

#指定元素赋值
classmates[1]='Sarah'
print(classmates)

#tuple 不能修改
classmates = ('Michael','Bob','Tracy')
print(classmates)

#注意 只有一个元素的元祖要加,
t = (1,)
print(t)
i = (1)
print(i)

#元祖中的数组可以改变
t = (1,2,['a','b'])
print(t)
t[2][0] = 'x'
t[2][1] = 'y'
print(t)