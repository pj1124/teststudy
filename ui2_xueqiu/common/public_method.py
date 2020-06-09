# _*_ coding:utf-8 _*_
# @Time: 2020/6/121:55
# @Author: Jerry

class PublicMethod:

    def modify_dict_value(self, you_dict, key_list, value):
        """
        用于修改字典中的value值，实现不确定长度字典的修改
        :param you_dict: 要修改的字典
        :param key_list:
        :param value:
        :return:
        """
        if type(you_dict) is not dict:
            msg = '所需要的参数应该是dict格式，请确认你的传参；you_dict：{}'.format(you_dict)
            raise TypeError(msg)
        if type(key_list) is not list:
            msg = '所需要的参数应该是list格式，请确认你的传参；key_list：{}'.format(you_dict)
            raise TypeError(msg)
        yaml_data = you_dict

        # 首先将字典逐级读取出来，写入到data_list中
        tem = None
        data_list = []
        for n in range(len(key_list)):
            try:
                if n == 0:
                    tem = yaml_data[key_list[n]]
                else:
                    tem = tem[key_list[n]]
            except Exception as e:
                msg = '源数据没有key-{}！error:{}'.format(key_list[n], e)
                raise TypeError(msg)
            data_list.insert(0, tem)

        # 修改需要修改的值后再封装字典
        new_dict = {}
        for m in range(len(key_list)):
            tem_dict = {}
            tem_list = []
            if m == 0:
                # 修改为需要修改的值
                tem_dict[key_list[-m - 1]] = value
            else:
                # 不修改的直接封装起来
                if isinstance(key_list[-m - 1], str):
                    tem_dict[key_list[-m - 1]] = new_dict
                elif isinstance(key_list[-m - 1], list):
                    tem_list = data_list[m + 1]
                    tem_list[key_list[-m - 1]] = new_dict
                else:
                    msg = '暂时不支持该数据格式！{}'.format(key_list[-m - 1])
                    raise TypeError(msg)
            new_dict = tem_dict

            if m == len(key_list) - 1:
                # 更新最外层的key
                yaml_data.update(new_dict)
                break
            else:
                # 逐层封装更新字典
                p = data_list[m + 1]
                if isinstance(p, dict):
                    p.update(new_dict)
                elif isinstance(p, list):
                    p = tem_list
                else:
                    msg = '暂时不支持该数据格式！{}'.format(p)
                    raise TypeError(msg)
                new_dict = p
        return yaml_data
