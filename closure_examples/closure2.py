def fun():
    i = 1

    def sub_fun(n):
        nonlocal i
        i = n
        print('sub_fun: the variable i  memory address {}'.format(id(i)))

    print('fun: before call sub_fun the variable i  memory address {}'.format(id(i)))
    sub_fun(4)
    print('fun: after call sub_fun, the variable i  memory address {}'.format(id(i)))

fun()