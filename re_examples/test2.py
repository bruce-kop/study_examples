'''
findall()和finditer()函数非常相似，它们的区别如下所示
    findall()：在输入字符串中查找所有匹配内容，如果匹配成功，则返回match子串列表，如果匹配失败则返回None
    finditer()：在输入字符串中查找所有匹配内容，如果匹配成功，则返回容纳match的可迭代对象，
                通过迭代对象每次可以返回一个match对象，如果匹配失败则返回None

'''

import re


p =r'[\\]ava'
text ='I like Java and java rava \\ava'

match_list =re.findall(p, text)
print(match_list)

match_iter =re.finditer(p, text)
print(match_iter)

for m in match_iter:
    print(m.group())

