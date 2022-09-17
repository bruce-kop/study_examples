
'''
静态方法
● 在方法前追加@staticmethod装饰器
● 静态方法可以被类和对象调用
● 静态方法不能调用对象属性和对象方法
对象方法
● 对象方法入参第一个值，默认self指代当前调用的对象；
● 只能被对象调用

类方法：
● 第一个参数是cls， 表示调用当前的类名。
● 在方法前追加@classmethod装饰器
● 可以被对象和类调用。
● 类方法不能调用对象属性和对象方法，但是可以调用静态方法
'''


import re

class VerifyUtil:
    @staticmethod
    def verify_phone(phone):
        # A regular expression for the mobile phone number format
        reg = '^1(3[0-9]|4[5,7]|5[0,1,2,3,5,6,7,8,9]|6[2,5,6,7]|7[0,1,7,8]|8[0-9]|9[1,8,9])\d{8}$'
        return re.match(reg, phone)

class Student(object):
    school = ""

    def __init__(self, stu_number="", full_name="", phone="", nationality=""):
        self.stu_number = stu_number
        self.full_name = full_name
        self.phone = phone
        self.nationality = nationality

    @staticmethod
    def is_chinese(nationality):
        if nationality == "china":
            return True
        else:
            return False

    @staticmethod
    def make_full_name(is_chinese, family_name, name):
        full_name = family_name + " " + name if is_chinese else name + " " + family_name
        return full_name

    def set_name(self, family_name, name):
        is_chinese = Student.is_chinese(self.nationality)
        self.full_name = Student.make_full_name(is_chinese, family_name, name)

    def set_phone(self, phone):
        if not VerifyUtil.verify_phone(phone):
            raise ValueError
        else:
            self.phone = phone

    def set_stu_number(self,stu_number):
        self.stu_number = stu_number

    def set_nationality(self,nationality):
        self.nationality = nationality

    @classmethod
    def set_school(cls):
        cls.school = 'Zhejiang University'


if __name__ == '__main__':
    #静态函数被类调用
    print(Student.make_full_name(True, "张", "三"))
    print(Student.make_full_name(False, "joson", "mike"))


    s1 = Student()
    # 静态函数被对象调用
    print(s1.make_full_name(True, "李", "四"))
    print(s1.make_full_name(False, "lee", "bruce"))








