#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : main.py
Author       : miaoyc
Create date  : 2021/9/18 10:54 下午
Description  : 
"""

import pandas as pd


def get_data_from_xls(file_path):
    return pd.read_excel(file_path)


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
    data = get_data_from_xls(file_path=test_data_file)
    print(type(data))
    print(data.colums)
    res = data.groupby('key').quantile()
    print(res)
