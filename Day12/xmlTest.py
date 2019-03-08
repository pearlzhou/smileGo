#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

import xml.dom.minidom



def getUer(parent,child=None):
	xmlFile=xml.dom.minidom.parse('data.xml')
	db=xmlFile.documentElement
	itemList=db.getElementsByTagName(parent)
	item=itemList[0]
	return item.firstChild.data
	# return item.getAttribute(child)

print(getUer('yan'))



























#
# def getXml(value):
# 	xmlFile=xml.dom.minidom.parse('data.xml')
# 	db=xmlFile.documentElement
# 	name = db.getElementsByTagName(value)
# 	valueName=name[0]
# 	return valueName.firstChild.data




