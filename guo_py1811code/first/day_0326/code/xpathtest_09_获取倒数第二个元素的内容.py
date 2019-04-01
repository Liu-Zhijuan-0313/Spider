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
from lxml import etree

html = etree.parse('hello.html')

result = html.xpath('//li[last()-1]/a')
# text 方法可以获取元素内容
print(result[0].text)
print(result)
result = html.xpath('//li[last()-1]/a/text()')
print(result)


