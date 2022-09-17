
def printName(ischinese, familyName, name):
    def inner_print(a,b):
        print("{0} {1}".format(a,b))

    if ischinese:
        inner_print(familyName,name)
    else:
        inner_print(name, familyName)


printName(True, '张', '三')
printName(False, 'zhang','bruce')

