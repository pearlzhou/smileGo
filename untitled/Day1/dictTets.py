#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

# dict1={'name':'wuya','age':20,'address':'xian'}

'''clear-->全部清空'''
# dict1.clear()
# print dict1

'''copy-->'''
# dict2=dict1.copy()
# print dict2

'''pop删除指定的key对应的value值，并且打印出来'''
# print dict1.pop('age')
# print dict1

'''判断key是否存在'''
# age=30
# if dict1.has_key('age'):
# 	if age>18:
# 		print dict1['age']
# else:
# 	print 'Sorry,no age key'


'''获取到字典中key对应的具体value值'''
# print dict1['age']
# print dict1.get('age')

'''获取到所有的key值'''
# for key in dict1.keys():
# 	print key

'''获取到所有的vakue值'''
# for value in dict1.values():
# 	print value

'''对字典循环'''
# for key,value in dict1.items():
# 	print key,':',value


'''字符串与列表之间的转换'''

# str1='ADMINyadmin'
# '''str-->list'''
# list1=str1.split('y')
# print list1,type(list1)
#
# '''list-->str'''
# print ','.join(list1)

'''list与tuple之间的转换'''
#
# list1=[1,2,3,4,5]
#
# '''list-->tuple'''
# tuple1=tuple(list1)
# print tuple1,type(tuple1)
#
# '''tuple-->list'''
# list2=list(tuple1)
# print list2,type(list2)

'''dict与list之间的转换'''

'''dict--->list'''
dict1={'name':'wuya','age':20,'address':'xian'}
list1=dict1.items()
print list1,type(list1)

'''list--->dict'''
dict2=dict(enumerate(list1))
print dict2,type(dict2)


dict3={"code":200,"msg":"成功!",
       "data":{"yesterday":
	               {"date":"28日星期六","high":"高温 37℃","fx":"东南风","low":"低温 26℃","fl":"\u003c![CDATA[3-4级]]\u003e","type":"多云"},"city":"西安","aqi":"66","forecast":[{"date":"29日星期天","high":"高温 37℃","fengli":"\u003c![CDATA[3-4级]]\u003e","low":"低温 26℃","fengxiang":"东北风","type":"多云"},{"date":"30日星期一","high":"高温 35℃","fengli":"\u003c![CDATA[\u003c3级]]\u003e","low":"低温 24℃","fengxiang":"东风","type":"阵雨"},{"date":"31日星期二","high":"高温 34℃","fengli":"\u003c![CDATA[\u003c3级]]\u003e","low":"低温 25℃","fengxiang":"东北风","type":"小雨"},{"date":"1日星期三","high":"高温 34℃","fengli":"\u003c![CDATA[3-4级]]\u003e","low":"低温 25℃","fengxiang":"东南风","type":"多云"},{"date":"2日星期四","high":"高温 34℃","fengli":"\u003c![CDATA[3-4级]]\u003e","low":"低温 25℃","fengxiang":"东南风","type":"多云"}],"ganmao":"各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。","wendu":"33"}}

'''
开放平台接口:https://www.apiopen.top/weatherApi?city=%E8%A5%BF%E5%AE%89
json在线：https://www.bejson.com/jsonviewernew/
数据:基于json格式的字符串类型的数据
一个标准：
1、业务状态码:code:200
2、消息:msg
3、数据:data

断言：
1.业务状态码:dict3['code]
2.数据:dict3['data']['forecast'][0]['high']
3.HTTP协议状态码的断言
'''
# #取到今天的温度
# print dict3['data']['forecast'][0]['high']