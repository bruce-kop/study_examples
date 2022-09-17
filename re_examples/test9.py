import re
import requests

if __name__ == '__main__':
    uri = 'https://www.qidian.com/lishi/'

    source = requests.get(uri)
    content_bytes = source.content
    conten_str = content_bytes.decode()

    re1 = "<div class=\"big-list cf\" data-l1=\"\d\">(.*?)</li>\s{2}</ul>\s</div>"

    matchObj = re.search(re1, conten_str, re.S)
    print(matchObj.group(1))
    re2 = "<h2><a href=\"(?P<href>.*?)\" data-eid=\".*?\" data-bid=\".*?\" " \
          "target=\".*?\" title=\"(?P<title>.*?)\">(.*?)</a></h2>"
    re2 = "<h2><a href=\"(?P<href>.*?)\" .*? title=\"(?P<title>.*?)\">.*?</a></h2>"
    datas = re.findall(re2, matchObj.group(1), re.S)
    print(type(datas))
    for s in datas:
        print(s)


