#re.M
'''
re.M: 多行匹配，影响 ^ 和 $

'''
import re

s='''I always think,
love is great,is all i have.
you should known me.
No one can love you more than me.
'''
print(re.findall("^\w+", s, re.M))         # 匹配位于行首的单词
print(re.findall('^\w+', s))         # 匹配位于字符串开头的单词
print(re.findall('(\w+).$', s, re.M))        # 匹配位于行尾的单词
print(re.findall('\w+.$', s))      # 匹配位于字符串尾的单词
print(re.match('你 好', '你好似懂非懂是', re.X).group())
print(re.search(r'\((\d+)\)', 'sdkjf(17)ja8379').group(1))