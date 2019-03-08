#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


name='WuYa'
age=18
address='xian'

#format

print 'my name is %s,age is %d, I come from %s'%(name,age,address)
print 'my name is {0},age is {1},i come from {2}'.format(name,age,address)
print 'my name is {:s},age is {:d},i come from {:s}'.format(name,age,address)
print 'my name is {name},age is {age},i come form {address}'.\
	format(name=name,age=age,address=address)
