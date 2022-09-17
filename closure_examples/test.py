n = 4
def func1(var):
    print("the func1 been call。")
    #n = 4
    def func2():
        nonlocal var
        global n
        var = 2
        n = 3

        print("the var is:%s"%var)
        print("the n is :%s"%n)
        print("fun2 var:{0}, n:{1}".format(id(var),id(n)))

    print("before var:{0}, n:{1}".format(id(var), id(n)))
    func2()
    print("after var:{0}, n:{1}".format(id(var), id(n)))
    print(n)
    print(var)

if __name__ == '__main__':
    func1(1)
    print(n)

