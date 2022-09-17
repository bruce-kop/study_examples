class NotEqual(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __repr__(self):
        return ("not equal:{}".format(self.msg))


if __name__ == '__main__':

    try:
        raise NotEqual('使用 raise 主动抛出异常。')
    except NotEqual as err:
        print("异常：{}".format(repr(err)))