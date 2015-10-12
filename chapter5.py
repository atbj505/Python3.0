#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用dict和set

d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}
print(d['Michael'])

d['Bob'] = 65
print(d)

#通过in判断key是否存在
print('Thomas' in d)
print('Bob' in d)

#通过get方法返回对应的value
print(d.get('Thomas',-1))
print(d.get('Bob'))

#pop 删除一个键值对
d.pop('Bob')
print(d)


# set
s = set([1,2,3,4])
print(s)

#add添加元素，可以重复添加，但没有效果
s.add(5)
print(s)
s.add(5)
print(s)

#remove删除元素
s.remove(5)
print(s)

#交集，并集
s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(s1 & s2)
print(s1 | s2)