# -*- coding: utf-8 -*-
# def func1(x, y):
#     return x*y
#
# print(func1(2,6))

func = lambda x,y:x*y#声明一个匿名函数
print(func(6,9))
#匿名函数一般是配合其他方法一起使用
data = list(range(10))
print(data)
for index,i in enumerate(data):
    data[index] = i*i
print(data)
#方式一
def func(n):
    return n*n

print(list(map(func,data)))
#方式二
new_data = list(range(10))
print(list(map(lambda n:n*n,new_data)))

