#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

import  os
import  sys

#创建文件mkdir
# os.mkdir('c:/log')
# os.rmdir('c:/log')

#对文件或者目录重新命名
# os.rename('c:/log','c:/newLog')

#对目录的处理
print u'当前文件的目录:',os.path.dirname(__file__)
print u'文件当前目录的上一级目录:',os.path.dirname(os.path.dirname(__file__))
print u'文件当前目录的上一级目录的上一级目录:',os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

#实现对Day3下login文件内容的读取
base_dir=os.path.dirname(os.path.dirname(__file__))

f=open(os.path.join(base_dir,'Day3/login'),'r')
print f.read()

'''请求参数是不确定的，可能有一个，可能有N个'''
#
# def f(*args,**kwargs):
# 	return kwargs
#
# print f(name='wuya',age='18')
#
# print f(name='wuya',age='18',address='xian')


'''
python执行路径搜索：
程序根目录:当前模块的目录--->Hello WuYA
环境变量:C:\Python27;C:\Python27\Scripts
标准库目录:C:\Python27\Lib-->Hello Lib
第三方库的目录:C:\Python27\Lib\site-packages--->Hello Login
'''

# import  index
#
# index.login()

'''
from Day3.day3Login import *
#
# index()

执行的时候，提示login模块不存在，或者说找不到，解决方案如下：
'''

base_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),'Day6')
#把Day3加到环境变量
print sys.path
sys.path.append(base_dir)

import  day6Login

print day6Login.index()