'''基于正则表达式的爬虫案例
最简单的爬虫程序
'''

import re
import requests

url = "https://www.qidian.com/lishi/"
source = requests.get(url)
content_bytes = source.content
content_str = content_bytes.decode()

re1 = "<div class=\"big-list cf\" data-l1=\"\d\">(.*?)</li>\s{2}</ul>\s</div>"
matchObj = re.search(re1, content_str)
print(matchObj.group(1))

re2 = "<h2><a href=\"(.*?)\" .*? title=\"(.*?)\">.*?</a></h2>"
datas = re.findall(re2, matchObj.group(1), re.S)
for d in datas:
    print(d)


