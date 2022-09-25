'''
为密码进行加密，把密文存储到数据库   md5加密
'''

import hashlib
from django.conf import settings

def md5(data_string):

    obj=hashlib.md5(settings.SECRET_KEY.encode('utf-8'))    #使用settings里面的SECRET_KEY作为salt
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()
