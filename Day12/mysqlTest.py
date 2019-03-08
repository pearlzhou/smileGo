#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

import  pymysql

#查询
def connMySQL():
	try:
		conn=pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='server',
			db='five')
	except Exception as e:
		return e.args
	else:
		cur=conn.cursor()
		sql='select * from user where id=%s'
		params=(1,)
		# 单个语句的查询
		# cur.execute(sql,params)
		# data=cur.fetchone()
		# print(data)
		cur.execute('select * from user ')
		data=cur.fetchall()
		# for item in data:
		# 	print(item)
		db=[item for item in data]
		print([item for item in data])
	finally:
		cur.close()
		conn.close()

#insert
def insertMySQL():
	try:
		conn=pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='server',
			db='five')
	except Exception as e:
		return e.args
	else:
		cur=conn.cursor()
		#单条语句的插入
		# sql='insert into user values (%s,%s,%s,%s) '
		# params=(3,'weike',18,'xian')
		#批量插入
		sql='insert into user values (%s,%s,%s,%s)'
		params=[
			(4, 'weike', 18, 'xian'),
			(5, 'weike', 18, 'xian')
		]
		cur.executemany(sql,params)
		conn.commit()
	finally:
		cur.close()
		conn.close()

#delete
def deleteMySQL():
	try:
		conn=pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='server',
			db='five')
	except Exception as e:
		return e.args
	else:
		cur=conn.cursor()
		sql='delete from user where id=%s'
		params=(3,)
		cur.execute(sql,params)
		conn.commit()
	finally:
		cur.close()
		conn.close()

class MySqlHelper:
	def conn(self):
		con=pymysql.connect(
			host='127.0.0.1',
			user='root',
			passwd='server',
			db='five')
		return con

	def get_one(self,sql,params):
		cur=self.conn().cursor()
		data=cur.execute(sql,params)
		result=cur.fetchone()
		return result

def checkValid(username,password):
	opera=MySqlHelper()
	sql='select * from login where  username=%s and password=%s'
	params=(username,password)
	return opera.get_one(sql=sql,params=params)

def info():
	username=input('请输入用户名:\n')
	password=input('请输入密码:\n')
	result=checkValid(username,password)
	if result:
		print('登录成功,昵称:{0}'.format(username))
	else:print('登录失败')

if __name__ == '__main__':
    info()






