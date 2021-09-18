#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : main.py
Author       : miaoyc
Create date  : 2021/9/18 10:54 下午
Description  : 
"""


def get_data(file_path):
    """
    获取数据
    :param file_path: 原始数据文件路径
    :return:
    """
    with open(file_path) as f:
        res = f.readlines()
    return res


if __name__ == "__main__":
    test_data_file = "../data/test1.xlsx"
    print(get_data(file_path=test_data_file))
