# -*-coding:utf-8-*-#

"""
    Created by Lishixin 2017/10/20

"""

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from blog.util.baseUtil import asrCount
convId = 'ddddddddd'
textFrom = 'baidu'
asrNum = 50
asrCount(convId, textFrom, asrNum)

# from django.core.signing import Signer
# signer = Signer()
# value = signer.sign('My string')
# print(value)


