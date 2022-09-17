class A:
    name = 'zs'
    age = 18


def print_name(self):
    print("hello {}".format(self.name))

def print_age(cls):
    print("age is {}".format(cls.age))

a = A()
setattr(A,'print_name',print_name)
setattr(A,'print_age',print_age)
getattr(A,'print_age')(A)


