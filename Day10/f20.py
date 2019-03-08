#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

import  unittest
import  HTMLTestRunner
import  os



class F20(unittest.TestCase):
	def test_001(self):
		self.assertEqual(1,1)

	def test_002(self):
		self.assertEqual(1, 1)

class F21(unittest.TestCase):
	def test_f20_001(self):
		self.assertEqual(1, 1)

	def test_f20_002(self):
		self.assertEqual(1, 1)

	def test_f20_003(self):
		self.assertEqual(1, 1)

	@staticmethod
	def suite():
		suites = unittest.TestLoader().discover(
			start_dir=os.path.dirname(__file__),
			pattern='f20.py',
			top_level_dir=None)
		return suites

if __name__ == '__main__':

	suite=unittest.makeSuite(F21)

	filename='recort.html'
	fp=open(filename,'wb')
	runner=HTMLTestRunner.HTMLTestRunner(fp,title='dddlll',description='')
	runner.run(suite)


	# fp=open('report.html','wb')
	# runner=HTMLTestRunner.HTMLTestRunner(
	# 	stream=fp,
	# 	title='测试数据',
	# 	description=''
	# ).run()
	# runner.run(F21.suite())

	# suite=unittest.TestLoader().discover(
	# 	start_dir=os.path.dirname(__file__),
	# 	pattern='f20.py',
	# 	top_level_dir=None)
	# unittest.TextTestRunner(verbosity=2).run(suite)

	# suite=unittest.TestLoader().loadTestsFromModule('f20.py')
	# unittest.TextTestRunner(verbosity=2).run(suite)

	# suite=unittest.TestLoader().loadTestsFromTestCase(F20)
	# unittest.TextTestRunner(verbosity=2).run(suite)

    # suite=unittest.TestSuite(unittest.makeSuite(F20))
    # unittest.TextTestRunner(verbosity=2).run(suite)
