#! -*- coding:utf-8 -*-
# @Author: Jerry

import os
import yaml

# 获取项目的绝对路径
project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 数据配置文件主路径
filepath = project_path + "\\config\\"


# 读取 configData.yaml 文件数据
def read_date(filename):
    with open(filepath + filename, 'rb') as f:
        return yaml.load(f, Loader=yaml.FullLoader)
