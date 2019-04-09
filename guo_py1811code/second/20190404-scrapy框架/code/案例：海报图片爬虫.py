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
import datetime
from lxml import etree
import os.path

url = 'http://pic.haibao.com/hotimage/'
headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
html = requests.get(url,headers=headers).text
html = etree.HTML(html)

ls = html.xpath('//div[@class="pagelibox"]//img/@data-original')
print(len(ls))
for link in ls:
    print(link)
    image = requests.get(link,headers=headers).content
    imageName = link.split('/')[-1]
    imageName = os.path.dirname(__file__) + '/images/haibao/'+imageName
    print(imageName)
    with open(imageName,'wb') as file:
        file.write(image)


# 异步请求加载新的图片
url = 'http://pic.haibao.com/ajax/image:getHotImageList.json?stamp='
page = 1
skip = 83

while page <= 5:
    GMT_FORMAT = '%a %b %d %Y %H:%M:%S GMT 0800'
    stamp = datetime.datetime.utcnow().strftime(GMT_FORMAT)+' (中国标准时间)'
    print('stamp:',stamp)
    full_url = url + stamp
    data = {
        'skip':skip
    }
    print('page:',page)
    data = requests.post(full_url,data=data,headers=headers).json()
    skip = data['result']['skip']
    html = data['result']['html']
    html = etree.HTML(html)
    ls = html.xpath('//div[@class="pagelibox"]//img/@originUrl')
    print('len:',len(ls))
    for link in ls:
        print(link)
        image = requests.get(link, headers=headers).content
        imageName = link.split('/')[-1]
        imageName = os.path.dirname(__file__) + '/images/haibao/' + imageName
        print(imageName)
        with open(imageName, 'wb') as file:
            file.write(image)

    page +=1



