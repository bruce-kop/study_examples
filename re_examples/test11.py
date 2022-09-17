import re
import requests

def get_html(url):
    '''
        dec:爬取网站html源码，返回字符串类型的数据
        @params：
            url：网站的网址
        '''
    source = requests.get(url)
    content_bytes = source.content
    content_str = content_bytes.decode()
    return content_str

def get_story_list(url):

    '''
    Dec:爬取起点小说网站的热点图书名称和文章链接
    :params：
        url：起点网站的网址
    :return 一个由元组组成的列表， 元组中的元素是小说的标题和链接
    '''
    storys_html = get_html(url)

    re1 = "<div class=\"big-list cf\" data-l1=\"\d\">(.*?)</li>\s{2}</ul>\s</div>"
    matchObj = re.search(re1, storys_html)
    re2 = "<h2><a href=\"(.*?)\" .*? title=\"(.*?)\">.*?</a></h2>"
    return re.findall(re2, matchObj.group(1), re.S)

def get_storys_catalogs(story_list):
    '''
    Dec：获取每本小说的目录
    :return: 一个由字典组成的列表
    '''

    storys_catalog_lists = list()
    for story in story_list:
        uri = "https:"+story[0] + '#Catalog'
        print(uri)
        story_html = get_html("https://book.qidian.com/info/1034868935/?WxUg5ztDmi=1662545061921#Catalog")
        print(story_html)
        re1 = "<ul class=\"cf\">(.*?)</ul>"
        match1 = re.search(re1, story_html, re.S)
        print(match1)
        re2 = '''<li data-rid=".*?">(.*?)</li>\s+'''
        matchs = re.findall(re2,story_html,re.S)
        if not matchs:
            break

        #print(matchs)

        story_catalogs = list()
        story_dict = {}

        for row in matchs:
            #print(row)
            re2 = '''<li data-rid=".*?">(.*?)</li>\s+'''
            match_strs = re.findall(re2,row,re.S)
            for m in match_strs:
                temp_chapter = {}
                tmp = re.search("<h2 class=\"book_name\"><a href=\"(.*?)\"  .*?>(.*?)</a></h2>",m,re.S)
                temp_chapter['href']=tmp.group(1)
                temp_chapter['chapter']=tmp.group(2)
                story_catalogs.append(temp_chapter)
            match_strs = None
        story_dict['title'] = story[1]
        story_dict['catalog'] = story_catalogs
        storys_catalog_lists.append(story_dict)

    return storys_catalog_lists

url = "https://www.qidian.com/lishi/"
story_list = get_story_list(url)
#print(len(story_list))
#print(story_list)
storys_catalog_lists = get_storys_catalogs(story_list)
#print(len(storys_catalog_lists))
#print(storys_catalog_lists)