'''
描述：装饰器，缓存函数结果的示例

'''

import time
import hashlib
import pickle

cache = {}

def is_obsolete(entry, duration):
    d = time.time() - entry['time']
    return d > duration


def compute_key(function, args, kwargs):
    key = pickle.dumps((function.__name__, args, kwargs))
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memorize(function):
        def __memorize(*args, **kwargs):
            key = compute_key(function, args, kwargs)

            if key in cache and not is_obsolete(cache[key], duration):
                print('we got a winner')
                return cache[key]['value']

            result = function(*args, **kwargs)
            cache[key] = {'value': result, 'time': time.time()}
            return result

        return __memorize

    return _memorize

@memoize(duration=2)
def add(a,b):
    return a+b

if __name__=='__main__':
    print(add(1,2))
    time.sleep(3)
    print(add(1, 2))

