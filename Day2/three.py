#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


'''全局变量与局部变量'''

# 全局变量
name = 'wuya'

def f1():
	#可以对全局变量做修改
	global  name
	name='weike'
	print name

f1()



# def f2():
# 	#局部变量
# 	name='admin'
# 	print name
#
# f2()
