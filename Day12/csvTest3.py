# -*- coding: utf-8 -*-
# @Time    : 2019/2/3 10:43
# @Author  : zhouzz
# @FileName: csvTest3.py

import  csv
import  requests

def readCsvList():
	with open('csv.csv','r') as f:
		reader=csv.reader(f)
		next(reader)
		for item in reader:
			print(list(item)[0])


def readCsvDict():
	with open('csv.csv','r') as f:
		reader=csv.DictReader(f)
		for item in reader:
			print(dict(item)['URL'])

'''通过接口测试的技术获取拉钩网平台的资料'''
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

def getHeaders():
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
		'Cookie':'JSESSIONID=ABAAABAAADEAAFI4E8E3DD2F7AEA65C581F7C8BC082571F; _ga=GA1.2.157963863.1549087017; user_trace_token=20190202135656-592c1038-26af-11e9-b899-5254005c3644; LGUID=20190202135656-592c13d0-26af-11e9-b899-5254005c3644; index_location_city=%E6%B7%B1%E5%9C%B3; ab_test_random_num=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168acc83e4845f-01a3d0b7519e5b-5d1f3b1c-2073600-168acc83e4a296%22%2C%22%24device_id%22%3A%22168acc83e4845f-01a3d0b7519e5b-5d1f3b1c-2073600-168acc83e4a296%22%7D; LG_LOGIN_USER_ID=069c346b17e39e4564c4bc4e5abfbf53c642d58777ad4b89524f518f1cd4780d; _putrc=675272641AE9D107123F89F2B170EADC; login=true; unick=%E5%91%A8%E7%8F%8D%E7%8F%A0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; TG-TRACK-CODE=index_hotsearch; WEBTJ-ID=20190202150417-168ad05ae8a54d-0dfd6b1800507-5d1f3b1c-2073600-168ad05ae8b7a3; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549087017,1549091057; gate_login_token=dfddc93962910c2913246c41e127cc7fe66be4e8ea7b1c8b0191416f41ab7126; _gat=1; LGSID=20190203103935-f1c39848-275c-11e9-836b-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20190203104137-3a5c976b-275d-11e9-b8a0-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549161698; SEARCH_ID=938c778d494b44e1b82119973be126c5',
		'Referer':'https://www.lagou.com/jobs/list_%E7%A7%BB%E5%8A%A8%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
	}
	return headers

def laGou(page=2):
	positions=[]
	r=requests.post(
		url=url,
		headers=getHeaders(),
		data={'first':False,'pn':page,'kd':'自动化测试工程师'},
		timeout=10)
	for i in range(0,15):
		city=r.json()['content']['positionResult']['result'][i]['city']
		#区
		district=r.json()['content']['positionResult']['result'][i]['district']
		#教育
		education=r.json()['content']['positionResult']['result'][i]['education']
		#工作年限
		workYear=r.json()['content']['positionResult']['result'][i]['workYear']
		#薪资
		salary=r.json()['content']['positionResult']['result'][i]['salary']
		#公司名称
		companyFullName=r.json()['content']['positionResult']['result'][i]['companyFullName']
		#公司大小
		companySize=r.json()['content']['positionResult']['result'][i]['companySize']
		#公司标签
		companyLabelList=r.json()['content']['positionResult']['result'][i]['companyLabelList']
		#工作标签
		positionLables=r.json()['content']['positionResult']['result'][i]['positionLables']
		position={
			'城市':city,
			'区域':district,
			"学历":education,
			"工作年限":workYear,
			"薪资":salary,
			"公司名称":companyFullName,
			"公司大小":companySize,
			"公司标签":companyLabelList,
			"工作标签":positionLables
		}
		positions.append(position)
	headers=['城市','区域','学历','工作年限','薪资','公司名称','公司大小','公司标签','工作标签']
	with open('lagou.csv', 'w', encoding='gbk', newline='') as f:
		writer = csv.DictWriter(f, headers)
		writer.writeheader()
		writer.writerows(positions)
	# for item in positions:
	# 	with open('lagou.csv','w',encoding='utf-8',newline='') as f:
	# 		writer=csv.DictWriter(f,headers)
	# 		writer.writeheader()
	# 		writer.writerows(positions)


laGou()
