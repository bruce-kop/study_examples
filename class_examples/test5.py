
'''
@property装饰器
作用：将方法变成属性调用，
使用场景：
1、在不改变属性封装类型的情况下，使得外部能够访问类的属性；
2、和直接调用属性相比，可以做跟多的工作，比如给属性增加过滤器
3、和使用set，get方法相比调用更加简洁。
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
        self.__full_name = full_name  #属性名字必须和方法名区分开，否则会死循环
        self.__phone = phone  #属性名字必须和方法名区分开，否则会死循环
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
    '''
    @property其实就是实现了getter功能； @xxx.setter实现的是setter功能；还有一个 @xxx.deleter实现删除功能
    定义方法的时候 @property必须在 @xxx.setter之前，且二者修饰的方法名相同（age()）
    如果只实现了 @property（而没有实现@xxx.setter），那么该属性为 只读属性
    '''
    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, family_name, name):
        is_chinese = Student.is_chinese(self.nationality)
        self.__full_name = Student.make_full_name(is_chinese, family_name, name)
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not VerifyUtil.verify_phone(phone):
            raise ValueError
        else:
            self.__phone = phone

    def set_stu_number(self,stu_number):
        self.stu_number = stu_number

    def set_nationality(self,nationality):
        self.nationality = nationality

    @classmethod
    def set_school(cls):
        cls.school = 'Zhejiang University'


if __name__ == '__main__':

    s1 = Student()
    try:
        s1.phone = '12345' #实例化的对象使用属性时，不是调用属性（s1.__phone），而是用的方法名（s1.phone）
    except Exception as e:
        print(e)

    s1.phone = '13712345678'

    print(s1.phone)







