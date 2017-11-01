# -*-coding:utf-8-*-#

"""
    Created by Lishixin 2017/10/20

"""

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.utils import timezone
from datetime import datetime
from blog.models import BiAsrCount



def asrCount(convId, textFrom, asrCount):
    now = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
    asrC = BiAsrCount(conv_id=convId, text_from=textFrom, asr_count=asrCount, update_time=now)
    asrC.save()

convId = 'ddddddddd'
textFrom = 'baidu'
asrNum = 50
asrCount(convId, textFrom, asrNum)

# from django.core.signing import Signer
# signer = Signer()
# value = signer.sign('My string')
# print(value)


