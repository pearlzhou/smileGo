#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

import  requests


#https://movie.douban.com/subject_search?search_text=%E6%97%A0%E6%B6%AF&cat=1002
# r=requests.get(url='https://movie.douban.com/subject_search?search_text=%E6%97%A0%E6%B6%AF&cat=1002')
paydata={'search_text':'无涯','cat':1002}
r=requests.get(url='https://movie.douban.com/subject_search',params=paydata)
print(r.status_code)
print(r.url)
# print(r.text)
# # print(r.content.decode('utf-8'))
# # print(r.url)
# # print(r.encoding)
# # print(type(r.json()))



