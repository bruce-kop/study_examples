def outer_fun():
    i = 1
    j = 2
    def inner_fun(n):
        nonlocal i
        nonlocal j
        j = 3
        i+=n

    return inner_fun

f=outer_fun()
f(3)

print(len(f.__closure__))
print(f.__closure__[0].cell_contents)
print(f.__closure__[1].cell_contents)

