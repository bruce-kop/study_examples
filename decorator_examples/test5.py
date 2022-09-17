'''
描述：装饰器，运行时校验--参数检验示例
'''

import re
from functools import wraps

class PhoneValidate(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return self.msg

def verify_phone(func):
    @wraps(func)
    def _verify_phone(*args,**kwargs):
        # A regular expression for the mobile phone number format
        reg = '^1(3[0-9]|4[5,7]|5[0,1,2,3,5,6,7,8,9]|6[2,5,6,7]|7[0,1,7,8]|8[0-9]|9[1,8,9])\d{8}$'
        phone = args[0]
        if not re.match(reg, phone):
            raise PhoneValidate("phone is validate.")
        else:
            func(*args,**kwargs)
    return _verify_phone

@verify_phone
def register_user(phone=None, pwd=None):
    print("user {} register success.".format(phone))
    return True

if __name__ == '__main__':
    try:
        register_user("13712345678","Abc123456++")
    except PhoneValidate as e:
        print("register faild:{}".format(repr(e)))
