#encoding=utf8
import sys

#BGK,UTF8都兼容ASCII码，也就是说数字和字母以及其他ASCII都是占用一个字节
print("unicode 整型","*"*30)
print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2**30))
print(sys.getsizeof(2**60))
print(sys.getsizeof(2**90))

print("unicode 字符串","*"*30)
print(sys.getsizeof(''))
print(sys.getsizeof('a'))
print(sys.getsizeof('ab'))
print(sys.getsizeof('abc'))
print(sys.getsizeof('中'))
print(sys.getsizeof('中国'))

print("utf8", "*"*30)
print(sys.getsizeof(''.encode("utf8")))
print(sys.getsizeof('杭'.encode("utf8")))
print(sys.getsizeof('杭州'.encode("utf8")))
print(sys.getsizeof('杭州'.encode("utf8")))
print("BGK","*"*30)
print(sys.getsizeof(''.encode("GBK")))
print(sys.getsizeof('杭'.encode("GBK")))
print(sys.getsizeof('杭州'.encode("GBK")))
print(sys.getsizeof('杭州'.encode("GBK")))