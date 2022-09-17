class NotEqual(Exception):
    pass
    '''
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return ("str:not equal:{}".format(self.msg))

    def __repr__(self):
        return ("repr:not equal:{}".format(self.msg))
    '''
if __name__ == '__main__':

    try:
        raise NotEqual()
    except NotEqual as err:
        print("异常：{}".format(err))
        print("异常：{}".format(repr(err)))
        print("异常：{}".format(str(err)))
