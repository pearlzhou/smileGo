#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


from selenium import  webdriver
import  unittest

class BaiduTest(unittest.TestCase):
	def setUp(self):
		print('start')

	def tearDown(self):
		print('end')

	def test_baidu_so(self):
		print('测试用例执行')

if __name__ == '__main__':
    unittest.main(verbosity=2)