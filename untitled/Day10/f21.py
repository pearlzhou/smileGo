#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


import  unittest
import  HTMLTestRunner

def add(a,b):
	return a+b

class Baidu(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_001(self):
		'''两个数之和'''
		self.assertEqual(add(2,3),5)

if __name__ == '__main__':
    testunit=unittest.TestSuite(unittest.makeSuite(Baidu))
    htmlFile='rcort.html'
    fp=open(htmlFile,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='',description='')
    runner.run(testunit)