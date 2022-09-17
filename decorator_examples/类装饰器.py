
'''
描述：虽然装饰器是用类实现的，但是最终用来替换原函数的对象，仍然是一个处在__call__方法里的闭包函数
'''

import time
import random
from functools import wraps

class Timer:
    """装饰器：打印函数的耗时
    :param print_args:是否打印发发那个发名和参数，默认为False
    """
    def __init__(self,print_args):
        self.print_args = print_args

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            '''
                desc:jdhfksjdf
                    @param:args,
            '''
            st = time.perf_counter()
            ret = func(*args, **kwargs)
            if self.print_args:
                print(f'"{func.__name__}",args:{args},kwargs:{kwargs}')
            print("time cost:{} seconds".format(time.perf_counter()-st))
            return ret
        return decorated

    def count_time(self,func):
        @wraps(func)
        def decorated(*args, **kwargs):
            st = time.perf_counter()
            ret = func(*args, **kwargs)
            if self.print_args:
                print(f'"{func.__name__}",args:{args},kwargs:{kwargs}')
            print("time cost:{} seconds".format(time.perf_counter() - st))
            return ret

        return decorated


@Timer(print_args=True)
def random_sleep():
    print("random")



if __name__ == '__main__':
    random_sleep()
    #timer = Timer(print_args=True)
    #fun = timer(random_sleep)
    #fun()



