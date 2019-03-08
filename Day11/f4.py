#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

import  requests

r=requests.get('http://www.baidu.com',timeout=6)


r=requests.get(url='https://www.12306.cn/mormhweb/',verify=False)
print(r.content.decode('utf-8'))



