#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

'''cookie的请求&session'''

import  requests


def getLoginHeader():
		headers={
			'UserAgent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
			'Content-Type':'application/x-www-form-urlencoded'}
		return headers

loginData={
	'email':'13484545195',
	'icode':'',
	'origURL':'http://www.renren.com/home',
	'domain':'renren.com',
	'key_id':1,
	'captcha_type':'web_login',
	'password':'8d9a71152919613bbe3df9bfa0e1b390eb2b13dd1bdde270c2816cf04dd1b7c5',
	'rkey':'b4cdc6acc1d36171e3de73dd4676208e',
	'f':'http%3A%2F%2Fname.renren.com%2F'}

def login():
	r=requests.post(
		url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201894216799',
		data=loginData,
		headers=getLoginHeader())
	return r.cookies


def getProfile():
	r=requests.get('http://www.renren.com/967004081/profile',cookies=login())
	print(r.text)

getProfile()
