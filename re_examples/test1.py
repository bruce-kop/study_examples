'''
re 模块的search和match对比和使用示例。
参数（pattern，string[,flags])
pattern：	匹配的正则表达式
string： 要匹配的字符串。
flags：标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

search()：在输入字符串中查找，返回第一个匹配内容，如果找到一个则match对象，如果没有找到返回None。
match()：在输入字符串开始处查找匹配内容，如果找到一个则match对象，如果没有找到返回None。

match对象有一些常用方法:
    group()方法返回匹配的子字符串；
    start()方法返回子字符串的开始索引；
    end()方法返回子字符串的结束索引；
    span方法返回子字符串的跨度，它是一个二元素的元组。

修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''

import re

p =r'\w+@jiakecong\.com'
text =r"Tony 's email is tony_guan111@Jiakecong.com。" \
      "bruce 's email is bruce@Jiakecong.com。"
s =re.search(p, text, re.S)
print(s)  #输出match=‘tony_guan111@jiakecong.com’
print(s.start())
print(s.end())
print(s.group())
print(s.span())

m =re.match(p, text)
print(m)

print("**"*30)


p =r'\w+@jiakecong\.com'
text ="tony_guan111@jiakecong.com, this is Tony 's email."
#match函数是从字符串开头开始匹配
m =re.match(p, text)
print(m) #输出None

print(m.start())
print(m.end())
print(m.group())
print(m.span())

def verify_pwd(pwd):
    reg = '^(?:' \
            '(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])|' \
            '(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])|' \
            '(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])|' \
            '(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])).{8,32}$'
    return re.match(reg, pwd)

def verify_phone(phone):
    # A regular expression for the mobile phone number format
    reg = '^1(3[0-9]|4[5,7]|5[0,1,2,3,5,6,7,8,9]|6[2,5,6,7]|7[0,1,7,8]|8[0-9]|9[1,8,9])\d{8}$'
    return re.match(reg, phone)

print("**"*30)

#search从左往右找，找最长匹配的字符串
p1 = r'a(.*)b'  #由r开头引起的字符串就是声明了后面引号里的东西是原始字符串, 在里面放任何字符都表示该字符的原始含义。
text ="a3234ba3234b778888a3234b"

m =re.search(p1, text)
print("search从左往右找，找最长匹配的字符串",m)
print(m.group(0))
print(m.group(1))

print("**"*30)
#(?P<name>)以及其引用(?P=name)的使用
p1 = r'a(?P<n>.*)ba(?P=n)b'  #由r开头引起的字符串就是声明了后面引号里的东西是原始字符串, 在里面放任何字符都表示该字符的原始含义。
text ="a3234ba3234b778888a3234b"

m =re.search(p1, text)
print(m)
print(m.group(0))
print(m.group('n'))


print(m.groups())
print("**"*30)

#(?:)的使用
p1 = r'a(?:.*)b'  #由r开头引起的字符串就是声明了后面引号里的东西是原始字符串, 在里面放任何字符都表示该字符的原始含义。
text ="a3234ba3234b778888a3234b"

m =re.search(p1, text)
print(m)
print(m.group(0))
try:
    print(m.group(1))
except IndexError as e:
    print(e)

print(m.groups())
print("**"*30)


#(?=)的使用
p1 = r'.*[.](?=bat$).*$'
text1 ="call.bat"
text2 ="call.exe"

m1 =re.search(p1, text1)
m2 =re.search(p1, text2)
print(m1.group())
print(m2)
print("**"*30)
#(?!)的使用

p1 = r'.*[.](?!bat$).*$'
text1 ="call.bat"
text2 ="call.exe"

m1 =re.search(p1, text1)
m2 =re.search(p1, text2)
print(m1)
print(m2.group())

print("**"*30)

p1 = r'.*[.](?!bat$|exe$).*$'
text1 ="call.bat"
text2 ="call.exe"

m1 =re.search(p1, text1)
m2 =re.search(p1, text2)
print(m1)
print(m2)


print("**"*30)

#出现n次{n}
p1 = r"(1212){2}"
text = "1212121212121212546475kjlkl"

m1 =re.search(p1, text)
print(m1)

print("**"*30)

#至少出现n次{n,}
p1 = r"(12){2,}"
text = "1212121212121212546475kjlkl"

m1 =re.search(p1, text)
print(m1)

print("**"*30)

#至少出现n次，最多m次{n,m}

p1 = r"(12){2,5}"
text = "1212121212121212546475kjlkl1212"

m1 =re.search(p1, text)
print(m1)

print("**"*30)
#+ * ?分别表示出现：出现一次或多次；出现0次或多次；出现0次或1次
p1 = r"(kl1212)?" #?是懒惰模式，获取最短的能满足条件的字符串
p2 = r"(12)+" #?是懒惰模式，获取最短的能满足条件的字符串
p3 = r"(12)*" #*是贪婪模式，获取最长的满足条件的字符串。
text = "1212121212121212546475kjlkl1212"
text2 = "fh12kshfoaf"
m1 =re.search(p1, text)
print(m1)
m2 =re.search(p2, text)
print(m2)
m3 =re.search(p3, text)
print(m3)