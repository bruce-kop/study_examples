'''

描述： 装饰器，替换复杂对象示例代码
'''


def func_replace(func):
    return fun_A

def class_replace(func):
    return B

def fun_A():
    print("fun_A")


@func_replace
def fun_B():
    print("fun_B")



class B(object):
    def __init__(self):
        print("class B")

    def print_str(self):
        print("hello world.")


@class_replace
class A(object):
    def __init__(self):
        print("class A")

    def print_int(self):
        print(5)

if __name__ == '__main__':
    fun_B()
    A().print_str()