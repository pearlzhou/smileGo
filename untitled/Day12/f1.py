#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

import pymysql

def connMySQL():
	conn=pymysql.connect(host='127.0.0.1',user='root',passwd='server',db='five')
	return conn

def get_one(sql,params):
	cur=connMySQL().cursor()
	result=cur.execute(sql,params)
	data=cur.fetchone()
	cur.close()
	connMySQL().close()
	return data

def checkValid(username,password):
	sql='select * from user where name=%s and address=%s '
	params=(username,password)
	return get_one(sql,params)

def info():
	username=input('请输入用户名:\n')
	password=input('请输入密码:\n')
	result=checkValid(username,password)
	if not result:
		print('用户名或者密码错误呀，请联系管理员')
	else:
		print('登录成功,用户名：{0}'.format(username))

info()
