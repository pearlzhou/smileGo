# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 18:08
# @Author  : zhouzz
# @FileName: f29.py
"重复数字前一个字符"
def convert(in_str):
    tmp = list()
    digit_list = [x if x.isdigit() else ' ' for x in in_str]
    digit_list = ''.join(digit_list)
    digit_list = [int(x) for x in digit_list.split()]

    alpha_list = [y if y.isalpha() else ' ' for y in in_str]
    alpha_list = ''.join(alpha_list)
    alpha_list = alpha_list.split()

    if in_str[0].isdigit():
        digit_list.remove(digit_list[0])
    while any(digit_list) and any(alpha_list):
        dig = digit_list[0]
        aph = alpha_list[0]
        cur = aph[:-1] + aph[-1] * dig
        tmp.append(cur)
        digit_list.remove(digit_list[0])
        alpha_list.remove(alpha_list[0])

    if any(alpha_list):
        tmp.append(alpha_list[0])

    return ''.join(tmp)


if __name__ == "__main__":
    str1 = 'a1b2c3d11e2f3g6'
    print(convert(str1))
    str2 = 'a1b2c3d11e2f3g6hgh'
    print(convert(str2))
    str3 = '11a1b2c3d11e2f3g6'
    print(convert(str3))
    str4 = '11a1b2c3d11e2f3g6hhh'
    print(convert(str4))
    str5 = '2132423423423'
    print(convert(str5))
    str6 = 'sfksdlfjsdklf'
    print(convert(str6))
