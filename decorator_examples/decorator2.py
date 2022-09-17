'''
描述：
    装饰器顺序：多个装饰器装饰的顺序是从里到外(就近原则)，而调用的顺序是从外到里（就远原则）。
    functools.wraps的作用：
        ● 装饰器会导致原始函数的元数据（名称，文档等属性）丢失。
         如果装饰器为原始函数增加额外属性或函数，那么就会出现找不到该属性或函数的情况。
        ● 只有使用了wraps，被原始函数的一些属性值可以赋值给修饰器函数。
'''

import time
import random
from functools import wraps

def timer(func):
    """装饰器：打印函数的耗时
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print("time cost:{} seconds".format(time.perf_counter() - st))
        return ret
    return decorated


def calls_counter(func):
    """
    装饰器记录函数被调用了多少次
    使用func.print_counter()可以打印统计到的信息
    """
    counter = 0
    def decorated(*args, **kwargs):
        nonlocal counter
        counter += 1
        print("calls_counter")
        return func(*args, **kwargs)

    def print_counter():
        print(f'Counter:{counter}')

    decorated.print_counter = print_counter
    return decorated


@timer
@calls_counter
def random_sleep():
    """让程序小睡一会 """
    return time.sleep(random.random())


if __name__ == '__main__':
    random_sleep()
    print(random_sleep.__name__)
    random_sleep.print_counter()


