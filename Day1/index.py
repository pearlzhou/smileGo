#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


# str1="无涯，您好！"
# # print type(str1)
#
# '''
# 问题：utf-8如何转为GBK的编码：
# 1.把utf-8解码成uncideo编码  decode()-->解码的时候，带着的编码是未解码前的编码格式
# 2.把unicode编码成gbk  encode()
# '''
#
# #把utf-8解码成unicode-->把str类型转为unicode
# strUnicode=str1.decode('utf-8')
# # print type(strUnicode)
#
# #把unicode转为gbk-->把uncide转为str
# strGbk=strUnicode.encode('gbk')
# print type(strGbk)
# print strGbk

from selenium import  webdriver

driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
str1=u'百度一下，你就知道'
print driver.title
assert  driver.title in str1
driver.quit()








