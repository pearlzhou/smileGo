# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 10:27
# @Author  : zhouzz
# @FileName: osTest.py

import os

def get_files(path=None, rule=".py"):
    all = []
    print os.walk(path)
    for root,dirs,files in os.walk(path):  # os.walk 是获取所有的目录
        for f in files:
            filename = os.path.join(root,f)
            if filename.endswith(rule):    # 判断是否是"xxx"结尾
                all.append(filename)
        return all


if __name__=='__main__':
    b = get_files(path=r"C:/Users/zhouzz/PycharmProjects/BB")
    for i in b:
        print(i)