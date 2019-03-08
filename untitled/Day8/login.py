#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

import  json
import  sys

class  Login(object):
	def __init__(self,username,passwd):
		self.usernane=username
		self.passwd=passwd

	def getUserName(self):
		return self.usernane

	def setUserName(self,username):
		self.usernane=username

	def getPasswd(self):
		return  self.passwd

	def setPasswd(self,passwd):
		self.passwd=passwd

	def register(self):
		'''注册功能的实现'''
		temp =self.usernane+'|'+self.passwd
		json.dump(temp, open('login', 'w'))
		print u'账号已注册成功,请开始登录'

	def login(self):
		f = str(json.load(open('login', 'r')))
		list1 = f.split('|')
		if list1[0] == self.usernane and list1[1] == self.passwd:
			return True
		else:
			return False

	def userInfo(self):
		f = str(json.load(open('login', 'r')))
		list1 = f.split('|')
		r = self.login()
		if r:
			print '恭喜{0}进入到系统'.format(list1[0])

		else:
			print 'Sorry，很遗憾，登录失败，请检查您的账号是否正确？'

	def exit(self):
		sys.exit(1)

per=Login('wuya','admn')

def main():
	'''主函数'''
	while True:
		try:
			t = int(raw_input('1、注册 2、登录 3、退出系统\n'))
		except  Exception as e:
			print e.args
		else:
			if t == 1:
				per.register()
			elif t == 2:
				per.userInfo()
			elif t == 3:
				per.exit()
			else:
				print u'输入错误，请继续输入，请输入1，或者2，或者3'
		finally:
			pass

if __name__ == '__main__':
    main()