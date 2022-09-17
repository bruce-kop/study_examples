from sys import getsizeof
class custom_iter:
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename,'r',encoding='utf8') as file:
            for line in file:
                yield int(line)



if __name__ == '__main__':
    ct = custom_iter('finle.txt')
    print(getsizeof(ct))

    filename = 'finle.txt'
    g = (int(line) for line in open(filename,'r',encoding='utf8'))
    print(getsizeof(g))
