'''
1.(?=)正向肯定断言（look ahead positive assert）或叫正前瞻
    作用：用于提取子字符串
    非捕获匹配模式，不保存匹配结果
    零宽度断言，不占用匹配位置
2.密码复杂度校验。
    要求密码至少包含三种字符以上，并且长度是8到32.
3.re.X ：提升正则表达式的可读性。
'''

import re


s = 'done run going'
p = re.compile(r'(?<!\bdo)\w+\b')

print('【Output】')
print(re.findall(p,s))
file = 'python.exe'


#密码复杂度检验
reg1 = re.compile(r'''^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])|
(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])|
(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])|
(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])).{8,32}$''')

r = re.compile('^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])).{8,32}$')
#匹配大写字母，小写字母，非数字字母至少3种以上，长度8到32
s = 'hd78Sr4545+'

print(r.match(s).group())


#re.X

#忽略正则表达式中的空格和注释，注释是以#开始引导的。
reg5 = re.compile(r'''^(?:#(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])#| #匹配大写字母，小写字母，数字至少3种以上，长度8到32
(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])|  #匹配大写字母，小写字母，非数字字母至少3种以上，长度8到32
(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])|
(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])).{8,32}$''',re.X)

s = 'hdSaj1jsh+'
print(reg5.match(s).group())
