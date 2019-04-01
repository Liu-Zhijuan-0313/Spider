"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/12'
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
import re
import requests

def down(url):
    head = {}
    #写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    response = requests.get(url,headers=head)
    html = response.content.decode()
    return html

if __name__ == "__main__":
    # 获取超链接<a>和</a>之间内容
    url = "https://www.baidu.com/"
    html = down(url)
    #print(html)
    pat = re.compile(r'<a .*?><span></span>(.*?)</a>',re.M|re.S)
    texts = pat.findall(html)
    for t in texts:
        print(t)