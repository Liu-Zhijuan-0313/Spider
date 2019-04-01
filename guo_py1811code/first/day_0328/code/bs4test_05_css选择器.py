"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/13'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,'lxml')
#通过标签名查找
print(soup.select('title'))
print(soup.select('a'))
print(soup.select('b'))
print(type(soup.select('b')[0]))
print(soup.select_one('a'))
print('==========================')
#通过类名查找
print(soup.select('.sister'))
print('==========================')
#通过 id 名查找
print(soup.select('#link1'))
print('==========================')
#组合查找
#p 标签中，id 等于 link1的内容，二者需要用空格分开

print(soup.select('p #link1'))
print(soup.select('body #link1'))
print('直接子标签查找:')
#直接子标签查找，则使用 > 分隔
print(soup.select("head > title"))
print(soup.select("body > p > a"))
print(soup.select("body > p > a#link2"))
print(soup.select("body > p > #link2"))
print(soup.select("body > p > .sister"))
print('==========================')
#属性查找
print('属性查找:')
print(soup.select('a[class="sister"]'))
print(soup.select('a.sister'))
print(soup.select('a[href="http://example.com/elsie"]'))
print(soup.select('p a[href="http://example.com/elsie"]'))
print('==========================')
print('属性获取:')
tag_a = soup.select_one('a[class="sister"]')
print(tag_a['class'])
print(tag_a.get('id'))
print(tag_a.attrs['href'])
print('==========================')
#获取内容
print('获取内容:')
soup = BeautifulSoup(html, 'lxml')
print(type(soup.select('title')))
print(soup.select('title')[0].get_text())
print(soup.select('title')[0].string)
for item in soup.select('body > p > a'):
    print(item.string)
    #print(item.get_text())




