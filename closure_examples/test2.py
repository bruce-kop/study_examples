def outer_fun():
    i = 1
    j = 9
    def inner_fun(n):
        nonlocal i
        nonlocal j

        i+=n
        j+=i
        print("inner",i,j)

    def inner_fun2():
        nonlocal j
        j = j+8

    return inner_fun, inner_fun2

f, f2= outer_fun()
f(3)
f2()

print("clobal ",f.__closure__[0].cell_contents)
print("clobal ",f.__closure__[1].cell_contents)
print("clobal ",f2.__closure__[0].cell_contents)

