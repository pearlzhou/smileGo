#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


'''
函数：函数是一段可以重复调用的代码，通过输入的参数，返回对应的结果
名字绑定的机制,把实际参数的值与形式参数的值名称绑定到一起
1.函数调用的时候，实际参数的值的顺序与形式参数的顺序一一对应
2.当在函数调用的时候，指定了形式参数的实际参数，这个时候并不是一一对应，而是根据指定的值来进行的
'''

# def add(a,b):
# 	print a+b
#
#
# add(3,2)
#
# add('wu','ya')
#
# add(b=3,a=2)

def info(name,age,address,sex):
	print u"name:{:s},age:{:d},地址:{:s},性别:{:s}".format(name,age,address,sex)

# info('wuya',18,'xian','boy')

def userInfo(userID):
	'''登录成功后，查看用户的基本信息'''
	pass


# def login(username='wuya',password='admin'):
# 	if username=='wuya' and password=='admin':
# 		print 'success'
# 	else:
# 		print 'fail login'
#
#
# login()
# # login('admin','admin')


# def name_age(name,age=18):
# 	pass

'''
函数的返回值：
1、一个函数，它是有返回值的
2、当一个函数，没return关键字的时候，它的返回值是None
3、当一个函数return关键字的时候，它的返回值是return后面的表达式或者值

函数的返回值意义：函数/方法的返回值是为了给另外一个函数/方法一个请求的参数而已
'''
'''
接口测试：查看用户信息  要查看，实现步骤：
1、发送post请求，login请求登录成功
2、登录成功之后了，返回token
3、带着这个token，可以查看用户信息
'''
def login(username='wuya',password='admin'):
	if username=='wuya' and password=='admin':
		return 'dsfhgjiopsd345987sddsf'
	else:
		return 'Login Fail'

def userInfo(token):
	'''查看用户信息'''
	if token=='dsfhgjiopsd345987sddsf':
		print u'显示无涯的订单信息'
	else:
		print 'logout'

userInfo(login())




