'''
描述：装饰器，注册函数示例
'''

class Register(dict):
    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        self._dict = {}

    def register(self, target):
        def add_register_item(key, value):
            if not callable(value):
                raise Exception(f"register object must be callable! But receice:{value} is not callable!")
            if key in self._dict:
                print(f"warning: \033[33m{value.__name__} has been registered before, so we will overriden it\033[0m")
            self[key] = value
            return value

        if callable(target):            # 如果传入的目标可调用，说明之前没有给出注册名字，我们就以传入的函数或者类的名字作为注册名
            return add_register_item(target.__name__, target)
        else:                           # 如果不可调用，说明额外说明了注册的可调用对象的名字
            return lambda x : add_register_item(target, x)

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __getitem__(self, key):
        return self._dict[key]

    def __contains__(self, key):
        return key in self._dict

    def __str__(self):
        return str(self._dict)

    def keys(self):
        return self._dict.keys()

    def values(self):
        return self._dict.values()

    def items(self):
        return self._dict.items()

register_functions = Register()

@register_functions.register
def add(a : int, b : int):
    return a + b

@register_functions.register("my multiply")
def multiply(a : int, b : int):
    return a * b

@register_functions.register
def minus(a : int, b : int):
    return a - b

if __name__=='__main__':
    print(register_functions)

    print(register_functions['add'](1,2))