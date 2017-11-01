# -*-coding:utf-8-*-#

"""
    Created by Lishixin 2017/10/20

"""

import os

def constantProxy(key):
    """
    从环境变量中读取参数，如果没有，再从项目配置文件中读取
    :param key: 系统参数key
    :return:
    """
    from blog.util.Constant import constDict
    return os.getenv(key, constDict[key])

