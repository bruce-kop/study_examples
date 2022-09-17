from contextlib import contextmanager
from socket import *
def create_conn(host,port,timeout = None):
    server = socket(AF_INET, SOCK_STREAM)
    srv_addr = (host, port)
    server.bind(srv_addr)
    server.listen(5)
    server.settimeout(timeout)  # 设置超时时间
    return server

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

class conn():
    def __init__(self,host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def __enter__(self):
        self.conn = create_conn(self.host, self.port, timeout=self.timeout)

        return conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('>>exit')
        if exc_type:
            #exc_type不为空表示with语句内部发生异常
            print(exc_val) #打印异常信息
            print(exc_tb)  #打印异常堆栈信息
            return True   #忽略异常
        self.conn.close()

if __name__ == '__main__':

    with create_conn_obj('127.8.8.8', 8000, timeout=6) as obj:
        print(type(obj))

    print("*"*30)
    with conn('127.8.8.8', 8000, timeout=6) as c:
        print("jhhh")



    print("end")