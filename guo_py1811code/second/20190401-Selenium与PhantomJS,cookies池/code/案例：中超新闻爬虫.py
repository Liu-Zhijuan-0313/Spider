#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import requests
import re

# 请求页面
headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
url = 'http://sports.163.com/zc/'
response = requests.get(url,headers=headers)
html = response.text
print(html)

# 数据提取
# 匹配新闻条目
pat1 = re.compile(r'<div class="news_item">.*?(<h3>.*?<div class="share">.*?</ul>.*?</div>.*?</div>).*?</div>',re.M|re.S)
# 匹配新闻标题
pat2 = re.compile(r'<h3>.*?<a.*?>(.*?)</a>', re.M | re.S)
# 匹配新闻链接
pat3 = re.compile(r'<h3>.*?<a.*?href="(.*?)">', re.M | re.S)
# 匹配标签
pat4 = re.compile(r'<div class="keywords">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>', re.M | re.S)
# 跟帖数
pat5 = re.compile(r'<a.*?class="comment">.*?<span class="icon">(.*?)</span>', re.M | re.S)
ls = pat1.findall(html)
print('len:',len(ls))
for item in ls:
    matchObj = pat2.search(item)
    if matchObj != None:
        title = matchObj.group(1)
    else:
        title = '空'
    print('title:', title)

    matchObj = pat3.search(item)
    if matchObj != None:
        news_url = matchObj.group(1)
    else:
        news_url = '空'
    print('news_url:', news_url)

    matchObj = pat4.search(item)
    if matchObj != None:
        tags = matchObj.group(1) + ','+matchObj.group(2)
    else:
        tags = '空'
    print('tags:', tags)

    matchObj = pat5.search(item)
    if matchObj != None:
        nums = matchObj.group(1)
    else:
        nums = '0'
    print('nums:', nums)

    print('='*60)




