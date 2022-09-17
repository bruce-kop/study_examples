'''
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python 的作用域一共有4种，分别是：
有四种作用域：
L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
G（Global）：当前脚本的最外层，比如当前模块的全局变量。
B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。
规则顺序： L –> E –> G –> B。
在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。
'''
from dis import *

class a:
    pass
g = a()
print("全局变量 g", g, id(g))
def func1(var):
    n = 4
    var = 0
    global g
    g = a()
    __name__ = "hello"
    def func2(n):
        nonlocal var
        if n%3 == 0:
            var = 1

        print("局部变量",var)

    print("局部变量 var",var,id(var))
    print("局部变量 g",g,id(g))
    print("内置变量 __name__",__name__,id(g))
func1(3)

