

class Meta(type):

    def __call__(cls, *args, **kwargs):
        print("entering Meta.__call__()")

        ins = super().__call__(*args, **kwargs)
        print("exiting Meta.__call__(): ", ins)
        return ins


class Foo(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print("entering Class.__new__()")
        rv = super().__new__(cls, *args, **kwargs)
        print("exiting Class.__new__()")
        return rv

    def __init__(self, *args, **kwargs):
        print("executing Class.__init__()")
        super().__init__(*args, **kwargs)


a = Foo()
print(a)
import sqlalchemy