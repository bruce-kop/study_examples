#本文详细阐述了
# 捕获分组（...），以及命名分组的使用；
# 非捕获分组（?:）,
# 正前瞻（?=...）,
# 反前瞻（?!），
# 正后顾 (?<=...),
# 反后顾(?<！...)的使用方法，并且给了详细的例子和视频解说。
#

import re

s = r'''The result of the matching subexpression that 
captures the group is temporarily stored in memory,
there has 3 group s'''
#正前瞻
#提取句子中的group，要求他的后面是单词is
p = re.compile(r'.*group (?=is)')
if m:=p.search(s):print("s匹配结果",m.group())

#匹配以bat后缀的文件
p1 = '.*[.](?=bat$).*?$'
s1 = 'server.bat'
if m:=re.search(p1,s1):print("s1匹配结果",m.group())

s2= 'server.batch'
s3 = 'server.exe'
if m:=re.search(p1,s2):
    print("s2匹配结果",m.group())
else:
    print("s2匹配失败")

if m:=re.search(p1,s3):
    print("s3匹配结果",m.group())
else:
    print("s3匹配失败")

#反前瞻
#提取句子中的group，要求他的后面不是单词is
p = re.compile(r'.*group (?!is)')
if m:=p.search(s):print(m.group())



#不匹配以bat和exe后缀的文件
p1 = '.*[.](?!bat$|exe$).*$'
s1 = 'server.batch'
if m:=re.search(p1,s1):print("s1匹配结果",m.group())

s2= 'server.bat'
s3 = 'server.exe'
if m:=re.search(p1,s2):
    print("s2匹配结果",m.group())
else:
    print("s2匹配失败")

if m:=re.search(p1,s3):
    print("s3匹配结果",m.group())
else:
    print("s3匹配失败")

#正后顾
#提取句子中的temporarily，要求他的前面是单词is
p = re.compile(r'(?<=is\s)temporarily')
if m:=p.search(s):print(m.group())

#反后顾
#提取句子中的temporarily，要求他的前面不是单词is
p = re.compile(r'(?<!is\s)temporarily')
if m:=p.search(s):print(m.group())


html = '''<li><a href="//www.qidian.com/kehuan/" target="_blank" data-eid="qd_A50">科幻</a></li>
<li><a href="//www.qidian.com/zhutianwuxian/" target="_blank" data-eid="qd_A50">诸天无限</a></li>'''
#捕获分组
#提取a标签的href属性和a标签的内容
p = '<a href=(.*?) .*?>(.*?)</a>'
print(re.findall(p, html))

p = '<a href=(?P<href>.*?) .*?>(?P<title>.*?)</a>'
print(re.search(p, html).group('href'),re.search(p, html).group('title'))
print(re.search(p, html).group(1),re.search(p, html).group(2))


#非捕获分组
p = '<a href=(?:.*?) .*?>(?:.*?)</a>'
print(re.findall(p, html))

p = '<a href=.*?>.*?</a>'
print(re.findall(p, html))
