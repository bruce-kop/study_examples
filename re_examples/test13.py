
#re.S的使用
'''re.S:使 . 匹配包括换行在内的所有字符. (.不匹配\r\n)
如果有re.S，那么正则表达式是将多行字符串当成一个完整的字符串来匹配。
如果没有re.S，那么正则表达式是一行一行匹配。
应用场景：爬虫程序中使用比较多

(.*?)  ()表示的是匹配分组
. 匹配任意字符
* 表示重复0次或多次
？ 表示非贪婪模式

'''

import re

strtemp = '''
<a href="/corrupt_report/" rel="nofollow" target="_self" role="menuitem" tabindex="-1">
廉洁举报</a>
<a href="https://renzheng.toutiao.com/guide?platform=%27PC%27&amp;source=%27www.toutiao.com%27" 
rel="nofollow" 
target="_blank" 
role="menuitem" 
tabindex="-1">企业认证</a>
<a href="https://hys.people-health.cn/m/#/pages/ncovSuff/index" 
rel="nofollow" target="_blank" role="menuitem" tabindex="-1">肺炎求助</a>
'''''
match_1 = re.findall('<a href=(.*?)rel',strtemp)
match_2 = re.findall('<a href=(.*)rel',strtemp,re.S)
print (match_1)
print(match_2)
print(len(match_2))

