import time
import random
from functools import wraps
def timer(func):

    """装饰器：打印函数的耗时 """

    @wraps(func)  # @wraps(view_func)的作用: 不改变使用装饰器原有函数的结构.
    def decorated(*arg, **kwargs):
        '''耗时计算装饰器'''
        st = time.perf_counter()
        ret = func(*arg, **kwargs)
        print("time cost:{} seconds".format(time.perf_counter()-st))
        return ret

    decorated.print_name = "name"
    return decorated

@timer
def random_sleep():
    """让程序小睡一会 """
    return time.sleep(random.random())


if __name__ == '__main__':
    random_sleep()
    print(random_sleep.__name__)
    print(random_sleep.__doc__)


