'''
类的魔法函数，是由解释器调用的，不需要用户程序来调用。
__call__
凡是可以将 () 直接应用到自身并执行，都称为可调用对象。
可调用对象包括自定义的函数、Python 内置函数以及实现了__call__函数的类的实例对象。

__str__和__repr__
两者都是将对象转化成字符串。
__str__ 面向用户，其目的是可读性；
__repr__ 面向的是python解释器，或者说开发人员，其目的是准确性。

'''
import json

class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __call__(self, emotion="happy"):
        print("name is {}".format(emotion))



    def __repr__(self):
        return "name:{0}, age:{1}, gender:{2}".format(self.name, self.age, self.gender)

    def __str__(self):
        s = {"name": self.name, "age":self.age, "gender":self.gender}
        s = json.dumps(s)
        return s


if __name__ == '__main__':
    p = Person('bruce', 23, 'men')
    p('sad')
    p()
    print(p)
