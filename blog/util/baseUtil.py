# -*-coding:utf-8-*-#

"""
    Created by Lishixin 2017/10/20

"""

import os
from django.utils import timezone
from blog.models import BiAsrCount
from datetime import datetime

def constantProxy(key):
    """
    从环境变量中读取参数，如果没有，再从项目配置文件中读取
    :param key: 系统参数key
    :return:
    """
    from blog.util.Constant import constDict
    return os.getenv(key, constDict[key])


def asrCount(convId, textFrom, asrCount):
    now = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
    asrC = BiAsrCount(conv_id=convId, text_from=textFrom, asr_count=asrCount, update_time=now)
    asrC.save()