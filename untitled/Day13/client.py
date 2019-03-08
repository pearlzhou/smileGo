#!/usr/bin/env python
#coding:utf-8 

#Author:WuYa



import requests
import shutil

def send_request(url):
    r = requests.get(url)
    return r.status_code

def visit_ustack():
    return send_request('http://www.ustack.com')


class Remove(object):
    def rmdir(self,path='c:/'):
        r=shutil.rmtree(path)
        if r==None :
            return 'success'
        else:
            return 'fail'

    def exists_get_rmdir(self):
        return self.rmdir()
