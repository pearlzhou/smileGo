# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 10:38
# @Author  : zhouzz
# @FileName: f31.py
str1 = "a1c2d3ffd12gfd5"
str2 = '11a1b2c3d11e2f3g6'
str3 = '11a1b2c3d11e2f3g6hh'
str4 = "a1b2c3d11e2f3g6hh"
def convert(in_str):
	dig_list=[x if x.isdigit() else ' ' for x in in_str]
	dig_join=''.join(dig_list)
	dig_list_new=[int(x) for x in dig_join.split()]

	alp_list=[y if y.isalpha() else ' ' for y in in_str]
	alp_join=''.join(alp_list)
	alp_list_new=[y for y in alp_join.split()]

	result=[]
	#讨论字符串是否以数字开头
	if in_str[0].isdigit():
		dig_list_new.remove(dig_list_new[0])
	while any(dig_list_new) and any(alp_list_new):
		tmp_str=alp_list_new[0]*dig_list_new[0]
		result.append(tmp_str)
		alp_list_new.remove(alp_list_new[0])
		dig_list_new.remove(dig_list_new[0])
	# 讨论字符串尾部是否以有未配对的字母
	if any(alp_list_new):
		result.append(alp_list_new[0])
	print ''.join(result)

convert(str1)
convert(str2)
convert(str3)
convert(str4)