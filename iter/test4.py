
from sys import getsizeof
def generator():
    for i in range(10):
        yield i


g1 = (n for n in range(100))
print(getsizeof(g1))
l = [n for n in range(100)]

print(getsizeof(l))
g = generator()
print(getsizeof(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

