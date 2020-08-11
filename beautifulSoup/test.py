import urllib.request
from bs4 import BeautifulSoup
import re  # 正则表达式模块


def test():
    url = "http://baike.baidu.com/view/284853.htm"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    print(re.compile('view'))
    print(soup.find_all(href=re.compile('view')))
    for each in soup.find_all(href=re.compile('view')):
        print(each.text, "->",
              ''.join(["http://baike.baidu.com", each["href"]]))


if __name__ == "__main__":
    g = re.search(r'FishC', 'I love FishC.com!')
    print(g)
