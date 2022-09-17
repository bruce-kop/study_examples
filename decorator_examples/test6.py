'''
描述：装饰器，注入额外参数示例
'''
def print_chinese(is_chinese=True):

    def _print_chinese(func):
        def decorator(*args, **kwargs):
            if is_chinese:
                print("This is a chinese name.")
            else:
                print("This is a foreign name")
            func(*args,**kwargs)
        return decorator
    return _print_chinese


@print_chinese(is_chinese=True)
def print_name(family_name,name):
    print("{0} {1}".format(family_name, name))

if __name__ == '__main__':
    print_name("张", "三")