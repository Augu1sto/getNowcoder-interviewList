import requests
from lxml import etree
import re

url='https://www.nowcoder.com/ta/review-frontend/review?page='
fname = 'nowcoder-前端面试题-HTML部分.md'
page_range = range(1,43) # 1-42页

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

#编写一个函数用于获取HTML源代码
def getHtml(url):                            #构建一个函数用于获取网页的源代码
    r=requests.get(url,headers=headers)                      #使用get请求，返回response对象
    r.encoding = "utf-8"
    return r.text

def getQ(html):
    '''
    获取问题，并加上 ## 标签
    '''
    question = html.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/text()')
    return "## "+question[0].strip() + '\n'

def getA(html):
    '''
    获取答案，存到列表里
    '''
    answer = html.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/p')
    if len(answer) == 0: # 没有p标签
        answer = html.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]')
    ret = []
    for a in answer:
        b = a.xpath('string(.)')
        # 处理空白符
        b = re.sub(r"\s+", "", b)
        if b.strip() !='':
            # 对标签进行转义
            b = re.sub(r"<","\<",b)
            ret.append('- '+b.strip()+'\n')
    return ret

def getD(html):
    '''
    获取讨论区链接
    '''
    pref = 'https://www.nowcoder.com'
    href = html.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/a/@href')
    return '[Discussion]('+pref+href[0]+')\n'


for page in page_range:
    t = getHtml(url+str(page))
    html = etree.HTML(t)
    with open(fname ,'a+') as f:
        question = getQ(html)
        f.write(question)
        answer = getA(html)
        for a in answer:
            f.write(a)
        f.write(getD(html))