#! -*- coding:utf-8 -*-
# @Author: Jerry
from appium_xueqiu.common.operation_yaml import read_date

data_list = read_date("search_data.yaml")
print(data_list)
print(type(data_list))
print(type(data_list[0]))
