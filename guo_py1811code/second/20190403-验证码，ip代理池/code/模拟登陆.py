"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/11'
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
# 获取一个有登录信息的Cookie模拟登陆
from urllib import request
import chardet

# 1. 构建一个已经登录过的用户的headers信息
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie
    "Cookie": "anonymid=jru48ifmt3j3si; _r01_=1; ln_uact=17752558702; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=757177d7-4364-40db-be6b-cdd5b17c1d81%7C077a3e2b1c00096d5c13732ceee74ce5%7C1549513361097%7C1%7C1551858470234; Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1553336590; _de=32B20555AD3784A6BF2D3D01B72FE013; depovince=HEN; jebecookies=d3962953-57b3-4d46-a4f0-e3a9705187fb|||||; JSESSIONID=abcTnGWfL0cHYezJXVGNw; ick_login=a442cbed-872a-4790-9324-391865743f49; p=8c6bc5dc598c34ee693781242ba434652; first_login_flag=1; t=4ef127a9b3a415546594dd2b76fa4a012; societyguester=4ef127a9b3a415546594dd2b76fa4a012; id=966924492; xnsid=1f40d058; ver=7.0; loginfrom=null; jebe_key=757177d7-4364-40db-be6b-cdd5b17c1d81%7C077a3e2b1c00096d5c13732ceee74ce5%7C1554253822374%7C1%7C1554253822232; wp_fold=0",
}

# 2. 通过headers里的报头信息（主要是Cookie信息），构建Request对象https://www.baidu.com/
req = request.Request("http://www.renren.com/966924492/", headers = headers)

# 3. 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），判断这是一个已经登录的用户，并返回相应的页面
response = request.urlopen(req)
# 4. 打印响应内容
html = response.read()
charset = chardet.detect(html)['encoding']
print(charset)
print(html.decode(charset))


