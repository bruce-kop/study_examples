# !python
# encoding = utf8
import time
import random
from functools import wraps


def timer(print_args=False):
    """装饰器：打印函数的耗时
    :param print_args:是否打印发发那个发名和参数，默认为False
    """

    def decorated(func):
        def wrapper(*arg, **kwargs):
            st = time.perf_counter()
            ret = func(*arg, **kwargs)
            if print_args:
                print(f'"{func.__name__}",args:{arg},kwargs:{kwargs}')
            print("time cost:{} seconds".format(time.perf_counter() - st))
            return ret

        return wrapper

    return decorated


@timer()
def random_sleep():
    """让程序小睡一会 """
    return time.sleep(random.random())


if __name__ == '__main__':
    random_sleep()
