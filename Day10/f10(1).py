#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

import  unittest
from Day10.init import *


class BaiduSo(Init):
	def test_baidu_news(self):
		self.driver.find_element_by_id('kw').send_keys('webdriver')

if __name__ == '__main__':
    unittest.main(verbosity=2)