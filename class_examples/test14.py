import re
class PhoneValidator():
    '''DEC:手机号格式合法验证器'''
    def __call__(self, *args, **kwargs):
        reg = '^1(3[0-9]|4[5,7]|5[0,1,2,3,5,6,7,8,9]|6[2,5,6,7]|7[0,1,7,8]|8[0-9]|9[1,8,9])\d{8}$'
        phone = args[0]
        if not re.match(reg, phone):
            print("phone is validate.")
        else:
            print("phone is invalidate.")


phone_validator = PhoneValidator()
#phone_validator("13735468254")
#phone_validator("10735468254")


class MetaC(type):
    def __init__(self,*args, **kwargs):
        super(A, self).__init__(args, kwargs)
        print("A")
    def __call__(self, *args, **kwargs):
        print("A call")
        return self

class Foo(object):
    __metaclass__=MetaC
    def __init__(self,*args, **kwargs):
        print("foo init.{} {} {}".format(self,args, kwargs))

f = Foo()

