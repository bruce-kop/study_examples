import sys

print(sys.getrefcount("dprint(sys.getrefcount([1,2]))"))

print(sys.getrefcount([1,2]))
a = [1,2]
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(a))
del b
print(sys.getrefcount(a))
c = a
print(sys.getrefcount(a))


class D:
    pass

class E:
    pass
d = D()
e = E()
d.name = e
e.name = d



print(sys.getrefcount(d))
print(sys.getrefcount(e))
del d
del e


q = 1

del q
print(globals())