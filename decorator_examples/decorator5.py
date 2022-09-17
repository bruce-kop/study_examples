'''
描述：类装饰器，类装饰器是装饰类的。
'''

def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwagrs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwagrs)
        return _instance[cls]

    return _singleton


@Singleton
class A:
    a = 1

    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':
    a1 = A(3)
    print(a1.a)
    print(a1.x)
    a2 = A(4)  # 该初始化无效，会返回a1，所以a2还是等于a1
    print(a2.a)
    print(a2.x)

