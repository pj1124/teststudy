# _*_ coding:utf-8 _*_
# @Time: 2020/6/120:53
# @Author: Jerry

import os
import yaml
from decimal import Decimal  # 如果yaml文件中有Decimal数据格式时需要有这个import

# 获取config目录的绝对路径
from ui2_xueqiu.common.public_method import PublicMethod

config_path = os.path.split(os.path.realpath(__file__))[0]


class Config:
    """
    # 统一封装YAML文件读写方法
    """

    def read_data(self, sign):
        """
            读取YAML文件数据
            @:param sign 文件名称(不包含文件后缀.yaml)
                # aws配置文件路径: base_aws_config.yaml
                # 基础接口url配置文件路径: base_url_config.yaml
                # 数据库配置文件路径: base_db_config.yaml
                # 数据删除脚本配置文件路径: base_delete_sql.yaml
                # 接口参数配置文件路径: base_interface_config.yaml
                # auth参数配置文件路径: encryption_config.yaml
                # easybuy的订单order相关配置: easybuy_order_data.yaml
                # 服务器servers相关配置: base_servers_config.yaml
            @:return config文件所有数据
        """
        file_path = os.path.abspath(os.path.join(config_path, sign+".yaml"))
        try:
            with open(file_path, 'rb') as f:
                return yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            msg = '配置文件读取异常，请确认你的文件名'
            raise Exception(msg)

    # 修改YAML文件数据--yaml配置文件需要是有两级数据
    def modify_data(self, sign, key_list, value):
        """
        修改配置文件
        :param sign: 文件名
        :param key_list: 修改的配置文件的层级目录，以list方式传入,[一级目录，二级目录，...]
        :param value: 需要修改的新值
        :return:
        """
        # # 定义白名单，白名单文件不允许修改
        # white_list = ['base_aws_config', 'base_db_config', 'base_delete_sql', 'base_servers_config', 'base_url_config', 'encryption_config']
        # if sign in white_list:
        #     return False

        data = Config().read_data(sign)
        # 保留一份旧文件，用于报错时恢复
        old_data = data
        file_path = os.path.abspath(os.path.join(config_path, sign + ".yaml"))

        try:
            with open(file_path, 'w', encoding="utf-8") as f:
                new_data = PublicMethod().modify_dict_value(data, key_list, value)
                yaml.dump(new_data, f)
        except Exception as e:
            # 如果发生报错时，恢复初始文件
            with open(file_path, 'w', encoding="utf-8") as f:
                yaml.dump(old_data, f)
            msg = 'modify data error:{}'.format(e)
            raise Exception(msg)

        return Config().read_data(sign)
