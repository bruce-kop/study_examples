def func1(var):
    print("the func1 been call。")
    n = 4
    def func2():
        nonlocal var
        nonlocal n
        var = 2
        n = 3

        print("fun2 var: {}, n:{}".format(id(var),id(n)))

    print("before fun2 var: {}, n:{}".format(id(var),id(n)))
    func2()
    print("after fun2 var: {}, n:{}".format(id(var),id(n)))

if __name__ == '__main__':
    func1(1)