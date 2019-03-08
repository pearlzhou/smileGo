#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

'''会话对象:Session'''

import  requests

def getHeader():
		headers={
			'UserAgent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
			'Content-Type':'application/x-www-form-urlencoded'}
		return headers

data={
	     'email':'13484545195',
	     'icode':'',
	     'origURL':'http://www.renren.com/home',
	     'domain':'renren.com',
	     'key_id':1,
	     'captcha_type':'web_login',
	     'password':'1511d3713664f271b68efaa96b9daf16241ea7d6654f4cf2ea2b3a492cb1c438',
	'rkey':'9c6be81661e35fd75af0f58feb8456ed',
	'f':'http%3A%2F%2Fzhibo.renren.com%2Ftop'}

def login():
	#对Session类进行实例化
	s=requests.Session()
	r=s.post(
		url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201894216799',
		data=data,
		headers=getHeader())
	return s

def getProfile():
	r=login().get('http://www.renren.com/967004081/profile')
	print(r.text)

getProfile()

