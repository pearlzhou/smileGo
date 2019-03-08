#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

import  requests
# from  requests.auth import HTTPBasicAuth

r=requests.get('http://localhost:5000/hotel/username/',
               auth=('wuya','admin'))
print(r.text)