#!/usr/bin/env python
#coding:utf-8 

#Author:WuYa

from Day13 import  client
from unittest import  mock
import  unittest


class MockTest(unittest.TestCase):
	def setUp(self):
		self.r=client.Remove()

	def test_fail_send(self):
		fail_send=mock.Mock(return_value='404')
		client.send_request=fail_send
		self.assertEqual(client.visit_ustack(),fail_send())

	def test_success_send(self):
		success_send=mock.Mock(return_value='200')
		client.send_request=success_send
		self.assertEqual(client.visit_ustack(),success_send())

	def test_remove_success(self):
		remove_success=mock.Mock(return_value='success')
		self.r.rmdir=remove_success
		self.assertEqual(self.r.exists_get_rmdir(),remove_success())

	def test_remove_fail(self):
		remove_fail=mock.Mock(return_value='fail')
		self.r.rmdir=remove_fail
		self.assertEqual(self.r.exists_get_rmdir(),remove_fail())

if __name__ == '__main__':
    unittest.main(verbosity=2)