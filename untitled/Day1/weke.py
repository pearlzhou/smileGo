#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


# str1='WUYAbwuya'
#
# list1=str1.split('b')
#
# str2=','.join(list1)
# print str2

dict1={'name':'wuya','age':10,'address':'xian'}

# for key in dict1:
# 	print key
#
# #对字典进行循环
# for key,value in dict1.items():
# 	print key,':',value
#
# print dict1.items()
#
# #判断是否在字典中
#
# print dict1.has_key('name')
#
# #使用fromkeys生成新的字典
# print dict1.fromkeys(['work'],('test',))
#
# tuple1=('android','ios','windows','firefoxos')
#
# print list(tuple1)

#字典到列表:
dict1={'name':'wuya','age':18,'address':'xian'}
list2=list(dict1.items())

#列表转为字典
print dict(enumerate(list2))