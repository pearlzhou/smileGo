# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 14:13
# @Author  : zhouzz
# @FileName: f30.py

#str1=input("请输入一个字符串：")
str1="a1c2d3ffd12gfd5"
str1_size=len(str1)
#找出字符串的数字单元
numbers=[]
i=0
while i < str1_size:
	num=''
	symbol = str1[i]
	while symbol.isdigit():
		num += symbol
		i += 1
		if i< (str1_size-1):
			symbol=str1[i]
		else:
			break
	i += 1
	if num != '':
		numbers.append(int(num))
print(numbers)
#找出字符串的字母单元
zimus=[]
j=0
while j < str1_size:
	zimu=''
	tmp_zimu = str1[j]
	while tmp_zimu.isalpha():
		print tmp_zimu
		zimu += tmp_zimu
		j += 1
		if j< (str1_size-1):
			tmp_zimu=str1[j]
		else:
			break
	j +=1
	if zimu != '':
		zimus.append(zimu)


print(zimus)
result=''
for m in range(len(zimus)):
	str_tmp=zimus[m]*numbers[m]
	result+=str_tmp
	print(result)
