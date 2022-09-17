def test_iter():
    list = [1, 2, 3, 4, 5]
    it = iter(list)
    print(next(it))
    print(next(it))

    return it

if __name__ == '__main__':
    it = test_iter()
    print(it)
    for x in it:
        print(x, end=" ")