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
from bs4 import BeautifulSoup
import json

def tencentSpider(page):
    # 网页爬取
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
    pn = (page-1)*10
    url = 'https://hr.tencent.com/position.php?&start=20' + str(pn)+'#a'
    response = requests.get(url,headers=headers)
    html = response.content
    print(html)
    # 数据提取
    html =BeautifulSoup(html,'lxml')
    results = html.select('table.tablelist > tr')
    results.pop(0)
    results.pop()
    print(len(results))
    items = []
    for each in results:
        item = {}
        td_ls = each.select('td')
        item['name'] = td_ls[0].select_one('a').string
        item['url'] = td_ls[0].select_one('a')['href']
        item['cate'] = td_ls[1].get_text()
        item['num'] = td_ls[2].get_text()
        item['city'] = td_ls[3].get_text()
        item['pub_date'] = td_ls[4].get_text()
        print(item)
        items.append(item)

    # 数据存储
    file = open('./tencent.json','a',encoding='utf-8')
    lines = json.dumps(items)
    file.write(lines)
    file.close()





if __name__ == "__main__":
    for i in range(1,6):
        tencentSpider(i)
