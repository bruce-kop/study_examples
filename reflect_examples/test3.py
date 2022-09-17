
'''
概念：反射就是通过字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员，一种基于字符串的事件驱动
可使用反射的地方：
    1、反射类中的变量 : 静态属性,类方法，静态方法
    2、反射对象中的变量、对象属性、普通方法
    3、反射模块中的变量
    4、反射本文件中的变量
反射的常用方法：
        1.hasaattr(obj,str)
            判断输入的str字符串在对象obj中是否存在(属性或方法)，存在返回True，否则返回False
        2.getattr(obj,str)
            将按照输入的str字符串在对象obj中查找。如找到同名属性，则返回该属性；如找到同名方法，则返回方法的引用，
            想要调用此方法得使用 getattr(obj,str)()进行调用。
            如果未能找到同名的属性或者方法，则抛出异常：AttributeError。
        3.setattr(obj,name,value)
            name为属性名或者方法名，value为属性值或者方法的引用
            1) 动态添加属性。如上
            2）动态添加方法。首先定义一个方法。再使用setattr(对象名,想要定义的方法名,所定义方法的方法名)
        4.delattr(obj,str)
            将你输入的字符串str在对象obj中查找，如找到同名属性或者方法就进行删除
应用场景：
    可以动态的向对象中添加属性和方法。也可以动态的调用对象中的方法或者属性。
'''

import re
import sys

class User(object):

    def __init__(self, name = "", pwd = ""):
        self.name = name
        self.pwd = pwd

    def __str__(self):
        return "name:{}, pwd:{}".format(self.name, self.pwd)

def login(self, name, pwd):
    if self.name == name and self.pwd == pwd:
        print("login success.")
    else:
        print('login faild.')

def set_nationality(cls,nationality):
    cls.nationality = nationality


def verify_pwd(pwd):
    reg = '^(?:' \
            '(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])|' \
            '(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])|' \
            '(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])|' \
            '(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])).{8,32}$'
    return re.match(reg, pwd)

if __name__ == '__main__':
    user = User("bruce", "123456")
    #给user对象添加gender这个对象属性
    setattr(user,"gender", "men")

    print(getattr(user,"gender"))
    #给类添加nationality这个类属性
    setattr(User,"nationality", "chinese")
    print(getattr(User,"nationality"))

    #给类添加对象方法
    setattr(user, "login", login)
    fun_login = getattr(user, 'login')
    fun_login(user,"bruce","123456")
    user.login(user, "bruce","123456")

    #给类添加类方法
    setattr(User, "set_nationality", set_nationality)
    User.set_nationality(User,"England")
    print(User.nationality)

    #给类添加静态方法
    setattr(User, "verify_pwd", verify_pwd)
    print(User.verify_pwd("123456Hi+"))

    #检查本文件中是否包含User，如果含有User，那么获取User
    if hasattr(sys.modules[__name__], 'User'):
        # sys.modulses[__ name__]就是本文件对象。
        print(getattr(sys.modules[__name__], 'User')())

    #删除属性id
    delattr(User, "nationality")

    User.nationality



