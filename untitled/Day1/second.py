#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:wuya


# a=3
# b='3'
# a='5'
# print a,type(a)

str1="ASFDasd"
# print dir(str1)
# print help(type(str1))

# print 'D在字符串的索引是第几位:',str1.index('D')
# print  '把字符串从小写转成大写:',str1.upper()
# print '大写--->小写:',str1.lower()
# print '字符串是以A开头:',str1.startswith('A')
# print '字符串是以d结束:',str1.endswith('d')

# print '字符串的替换:',str1.replace('asd','ASD')
# print str1.find('F')

#实现字符串转为列表的类型
list1=u'字符串--->列表:',str1.split('D')
# print list1


'''
单引号与双引号的区别:
1.在单引号中不能使用单引号
2.在双引号中不能使用双引号
3.在单引号中可以使用双引号
4.在双引号中可以使用单引号
'''
# str2='"a"'
# print str2

str3="'b'"
print str3

str4="\"a\""
print str4

str5='\'G\''
print str5

str6='''WuYa'''
print str6

def f1():
	'''aaa'''
	print 'hello'

f1()

