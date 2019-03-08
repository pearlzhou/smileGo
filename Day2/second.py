#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

# def f1(name):
# 	print u'用户基本信息:',name
#
# f1('name')
'''
*args:-->数据类型是元组
**kwargs->字典

'''


def f2(*args):
	print args,type(args)


def f3(**kwargs):
	print kwargs,type(kwargs)

def f4(name,age,sex,**kwargs):
	print u'用户信息:',name,age,sex,kwargs

f4('wuya',18,'boy')
f4('wuya',18,'boy',code='4876790608',phone='134r67',address='xian')
f4('wuya',18,'boy',
   code='4876790608',phone='134r67',address='xian',work='test',)

def f5(*args,**kwargs):
	print args,kwargs

f5()
f5(2)
f5('admin')
f5(['a','b'])
f5(address='xian')
f5(('a','b'))
f5({'name':'wuya','age':18})
f5(78.9)

def f6(name):
	print name

f6({'name': 'wuya', 'age': 18})

# f6()
# f6(2)
# f6('admin')
# f6(['a','b'])
# f6(address='xian')
