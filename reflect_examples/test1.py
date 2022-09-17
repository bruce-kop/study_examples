import sys
class A:
    def __repr__(self):
        return '666'
if hasattr(sys.modules[__name__],'A'):
    #sys.modulses[__ name__]就是本文件对象。
    print(getattr(sys.modules[__name__],'A')())