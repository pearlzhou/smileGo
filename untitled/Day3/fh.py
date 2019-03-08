#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

'''
根据字符串的形式去某个模块中寻找XX函数--->getattr()
根据字符串的形式去某个模块中判断东西是否存在--->hasattr()
根据字符串的形式去某个模块中设置东西---->setattr()
根据字符串的形式去某个模块中删除东西---->delattr()
'''

# #通过__import__导入目标模块并且放在一个对象中
# f=__import__('login')
# #通过对象找login模块中index的字符串并且调用
# f.index()
# f.info()

import  day3Login

# #调用login模块中的logout函数
# f=getattr(login,'logout')
# f()

#如何找到Person中的info方法并且调用它
# obj=login.Person()
# if hasattr(obj,'info'):
# 	f=getattr(obj,'info')
# 	f()
# else:
# 	print u'sorry'

# obj=login.Person()
# f=setattr(obj,'exit','this is a  exit method')
# f2=hasattr(obj,'exit')
# print u'setattr后的结果:',f2

# f=getattr(login,'str1')
# print f

# f=delattr(login,'str1')
# print f
# f2=hasattr(login,'str1')
# print f2


# #在login模块中设置变量str2
# f=setattr(login,'str2','hello world')
# #判断str2是否存在
# f2=hasattr(login,'str2')
# print f2

# #在login模块中删除str1
# f1=hasattr(login,'str1')
# print u'未删除str1前的结果:',f1
# f2=delattr(login,'str1')
# f3=hasattr(login,'str1')
# print u'删除后str1前的结果:',f3

url=raw_input(u'请输入路由地址:\n')
target_models,target_function=url.split('/')
m=__import__(target_models)
if hasattr(m,target_function):
    target_function=getattr(m,target_function)
    target_function()
else:
    print 'Not Found 404 Page'

    
