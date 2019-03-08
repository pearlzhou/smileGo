#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

'''
tuple-->不可变的，但是元组里面的元素的数据是可以变化
'''

tuple1=(1,2,3,4,3,[1,2,3],{'name':'wuya'})

# print dir(tuple1)

# '''count-->元素在元组中出现的次数'''
# print tuple1.count(3)
#
# '''index-->元素在元组中的索引'''
# print tuple1.index(4)

'''把元组中的列表由[1,2,3]修改为[1,2,3,4]'''
# tuple1[5].insert(3,4)

'''把元组中的字典name修改为weike'''
tuple1[6]['name']='weike'
print tuple1

