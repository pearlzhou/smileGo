#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya

'''
open()函数的参数：
1.要操作的文件名称
2.以什么样的方式操作文件

r:只读模式
w:只写模式【不可读，不存在就创建，存在就清空内容】
x:只写模式【不可读，不存在就创建，存在就报错】
a:增加模式【可读，不存在就创建，存在只增加内容】

"+"表示可以同时读写某个文件，具体为：

r+：读写

w+：写读

x+：写读

a+：写读
'''

'''w--->写文件'''
# f=open('file.json','w')
# temp={
# 	"name":"wuya",
# 	"age":20,
# 	"address":"xian"
# }
# # f.writelines(temp)
# f.close()

# import  json
# json.dump(temp,open('file.json','w'))

# f=open('c:/file1.txt','w')
# f.write('wuya')
# f.close()

'''r-->读
read()-->读取文件的所有内容
readlines()-->按行读取文件的内容,默认读取到文件的第一行
read(7)()-->只读取文件中某些字符,见案例的代码：
f=open('file1','r')
print f.read(7)
'''

# f=open('file1','r')
# for i in f.readlines():
# 	print i

# f=open('file1','r')
# print f.read()

# f=open('file1','r')
# print f.read(7)

'''追加'''
# f=open('file.json','a')
# f.write('wuya')
# f.close()

'''文件的上下文的处理'''
# with open('file2','w') as f:
# 	f.write('wuya')


