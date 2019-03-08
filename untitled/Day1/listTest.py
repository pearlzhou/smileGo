#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


list1=[1,2,0,8,4,6,9]

# print dir(list1)
# print help(type(list1))


# #insert--->把元素插入到第几位
# list1.insert(4,5)
# print list1

# #count-->在列表中出现了几次
# print list1.count(3)


'''index-->索引'''
# print list1.index(3)

'''pop-->默认删除最后一位并且打印出来'''
# print list1.pop()
# print list1

'''remove-->指定要删除的元素'''
# list1.remove(6)
# print list1

'''reverse-->反转'''
# list1.reverse()
# print list1

'''sort-->排序(从小到大)'''
# list1.sort()
# print list1

'''extend--->合并'''
# list2=['admin','wuya']
# list1.extend(list2)
# print list2
# print list1
#
# list2.extend(list1)
# print list2
# print list1

'''dir在自动化测试中的应用'''
from selenium.webdriver.common.alert import Alert

print dir(Alert)