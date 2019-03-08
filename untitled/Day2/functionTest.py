#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


#abs-->取绝对值
# print abs(-20)

#dir()--->查看方法
#type()

'''
匿名函数:lambda
在lambda的函数中，冒号左是形式参数，右是表达式
'''

# # def add(a,b):
# # 	return a+b
#
# add=lambda a,b:a+b
#
# print add(2,3)
# print add

'''
map()-->
'''

# list1=[1,2,3,4,5]
#
#
# def f1(a):
# 	return a+10
#
# # res=map(f1,list1)
# # print res
#
# res=map(lambda a:a+10,list1)
# print res

'''filter()-->过滤'''
# list1=[1,2,3,4,5,6,7,8,9,10]

# def f1(a):
# 	if a>3:
# 		return a
# # res=filter(f1,list1)
# # print res
#
# res=filter(lambda s:s>3,list1)
# print res

#id()--->查看内存
# a=2
# b=2
# print id(a)
# print id(b)

#isinstance
# str1=234
# print isinstance(str1,str)

#max()
#min()
#sum()

# list1=[1,2,3,4,5]
#
# print max(list1)
# print min(list1)
# print sum(list1)

#字母转数字

str1='a'
print ord(str1)

#数字转字母

str2=90
print chr(str2)