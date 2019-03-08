#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:zhouzz


'''
1、模拟登陆
2、模拟登陆成功显示登录成功后的用户账号
3、模拟注册
'''

def typeUsername():
	username=raw_input('请输入账号：\n')
	return username

def typePassword():
	password=raw_input('请输入账号密码：\n')
	return password

def regetist(username,password):
	'''
	实现注册的功能
	:parameter username:注册系统的账号
	:parameter password:注册系统的密码
	'''
	temp=username+'|'+password
	f=open('login','w')
	f.write(temp)
	f.close()

def login(username,password):
	'''
	登录
	:parameter username:登录系统的账号
	:parameter password:登录系统的账号密码
	'''
	f=open('login','r')
	for line in f:
		#把字符串转为list
		list=line.split('|')
		if list[0]==username and list[1]==password:
			return True
		else:
			return False

def info(username,password):
	'''
	系统登陆后的用户信息页面
	:parameter username:登录系统的账号
	:parameter password:登录系统的账号密码
	'''
	f=open('login','r')
	for line in f:
		#把字符串转为list
		list=line.split('|')
	r=login(username,password)
	if r:
		print '恭喜{0}进入到系统'.format(list[0])

	else:
		print 'Sorry，很遗憾，登录失败，请检查您的账号是否正确？'

def exit():
	'''退出系统'''
	import  sys
	sys.exit(1)

def main():
	'''主函数'''
	while True:
		t=int(raw_input('1、注册 2、登录 3、退出系统\n'))
		if t==1:
			username =typeUsername()
			password =typePassword()
			regetist(username,password)
		elif t==2:
			username = typeUsername()
			password =typePassword()
			login(username,password)
			info(username, password)
		elif t==3:
			exit()
		else:
			print '输入错误，请继续输入'

main()

