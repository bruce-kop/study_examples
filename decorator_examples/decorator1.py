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
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == '__main__':
    fact(10)



