class A():
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("B")

class C(A):
    def __init__(self):
        super(C, self).__init__()
        print("C")

class D(B,C):
    def __init__(self):

        super(B, self).__init__()
        print("D")

D()
print(D.__mro__)
