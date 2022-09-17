'''
compile(pattern, flags=0)
将正则表达式res编译成一个正则对象并返回,以便复用，可以提高速度。
但是从python的源码看，其实compile以及被集成到其他函数中，
比如findall中就调用了compile，所以re.compile（）是完全没有必要的，可以作为了解。
'''