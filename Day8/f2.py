#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


# class Fruit(object):
# 	def __init__(self,color):
# 		self.color=color
#
# class Apple(Fruit):
# 	def __init__(self,color):
# 		Fruit.__init__(self,color)
#
# apple=Apple('red')

class Person(object):
	def __init__(self,name):
		self.name=name

	def info(self):
		print self.name

class Son(Person):
	# def __init__(self,name):
	# 	Person.__init__(self,name)

	def __init__(self,name):
		super(Son,self).__init__(name)

son=Son('zhouzz')
son.info()
