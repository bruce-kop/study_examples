def outer_fun():
    i =1

    def inner_fun(n):
        nonlocal i
        i = i+n
        j = 2
        print("inner_fun: {} {}".format(i, j))

        def inner_inner_fun(m):
            nonlocal j
            nonlocal i

            i = i + 1
            j = j + 1

            print("inner_inner_fun: {} {}".format(i, j))

        return inner_inner_fun
    return inner_fun

inner_fun = outer_fun()

inner_inner_fun = inner_fun(3)

inner_inner_fun(4)