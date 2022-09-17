
from contextlib import contextmanager

def create_conn(host,port,timeout = None):
    conn = open('finle.txt','w')
    return conn

@contextmanager
def create_conn_obj(host,port, timeout = None):
    """创建链接对象，并且再退出上下文时自动关闭"""

    conn = create_conn(host,port,timeout = timeout)
    try:
        yield conn  #以yield关键字为界，yield前的逻辑会进入管理器时执行，
        #yield后的逻辑会在退出管理器时执行
    finally:   #如果要处理上下文管理器内处理异常，必须用try语句块包裹yield语句
        conn.close()
        print('close conn')

if __name__ == '__main__':

    with create_conn_obj('127.8.8.8', 8000, timeout=6) as obj:
        print(type(obj))


    print("main exit.")