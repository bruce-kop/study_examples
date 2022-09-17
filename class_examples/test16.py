class MataFoo(type):
    def __init__(self,*args, **kwargs):
        super(MataFoo, self).__init__(*args, **kwargs)
        print("MataFoo {}".format(args))

    def __call__(cls, *args, **kwargs):
        print("MetaFoo call {}, {}, {}".format(cls,args,kwargs))
        rv = super().__call__(*args, **kwargs)
        return rv

    def __new__(cls, *args, **kwargs):
        rv = super().__new__(cls, *args, **kwargs)

        print("MataFoo.__new__{} {} {}".format(cls, args, kwargs))
        return rv

class SubFoo(metaclass=MataFoo):
    def __new__(cls, *args, **kwargs):
        rv = super().__new__(cls, *args, **kwargs)
        print("Foo.__new__")
        return rv
    def __init__(self):
        super(SubFoo, self).__init__()
        print("Foo.__init__")

sub = SubFoo()