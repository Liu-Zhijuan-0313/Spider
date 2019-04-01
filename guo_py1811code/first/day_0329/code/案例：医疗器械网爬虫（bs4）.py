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
import pymongo
import re

def down(url):
    '''
    实现页面爬取
    :param url:
    :return:
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
    response = requests.get(url, headers=headers)
    html = response.text
    return (html,response.url)


def get_cate():
    '''
    实现分类的爬取
    :return:
    '''
    url = 'http://www.chinamedevice.cn/'
    html,cur_url = down(url)
    soup = BeautifulSoup(html,'lxml')
    ls = soup.select('a.f12')
    print(len(ls))
    base_url = 'http://www.chinamedevice.cn/'
    for item in ls:
        cate_url = base_url + item['href']
        print(cate_url)
        get_product_list(cate_url)




def get_product_list(cate_url):
    '''
    实现产品列表爬取
    :param cate_url:
    :return:
    '''
    html,cur_url = down(cate_url)
    soup = BeautifulSoup(html,'lxml')
    product_ls = soup.select('.list > ul > li')

    for item in product_ls:
        purl = item.select_one('h3 > span > a').get('href')
        get_product(purl)

    # 处理翻页
    pat_1 = re.compile(r'(\d+\.html)')
    page_btn = soup.select('.fno')
    if len(page_btn)>0:
        next_url = page_btn[-1].attrs['href']
        new_url = pat_1.sub(next_url,cur_url)
        print('next url:',new_url)
        get_product_list(new_url)

def get_product(url):
    '''
    提取产品信息
    :param url:
    :return:
    '''
    html,cur_url = down(url)
    soup = BeautifulSoup(html,'lxml')
    pname = soup.select_one('#main > dl > dt > h1').get_text()
    print('产品名称：',pname)
    print('url:',url)
    cover_url = soup.select_one('.img > a > img').get('src')
    print('cover_url:',cover_url)

    items = soup.select('.text01 > ul >li')
    cate_name = items[1].contents[1].strip()
    print('产品分类:',cate_name)
    number = items[3].contents[1].text.strip()
    print('批准文号:',number)

    spec = items[4].contents[1].strip()
    print('主要规格：',spec)

    description = soup.select_one('.text03').text.strip()
    print('产品说明：',description)

    producter = soup.select_one('.bgwhite.pt > h3 > a').text.strip()
    print('生产企业：', producter)

    contactor = soup.select('.text04 > ul > li')[2].text.split('：')[1]
    print('联系人：', contactor)

    phone = soup.select('.text04 > ul > li')[3].contents[0].strip().split('：')
    if len(phone) == 2:
        phone = phone[1]
    else:
        phone = '无'
    print('电话号码：', phone)

    address = soup.select('.text04 > ul > li')[9].text.split('：')
    if len(address)==2:
        address = address[1]
        print('单位地址：', address)

    print('='*60)

    item ={}
    item['pname'] = pname
    item['purl'] = url
    item['cover_url'] = cover_url
    item['cate_name']  = cate_name
    item['number'] = number
    item['spec'] = spec
    item['descition'] = description
    item['producter'] = producter
    item['contactor'] = contactor
    item['phone'] = phone
    item['address'] = address

    collec_ylqx.insert(item)


def get_collection():
    '''
    获取mongodb数据库集合
    :return:
    '''
    server = 'localhost'
    port = '27017'
    dbname = 'admin'
    user = 'admin'
    pwd = '123'
    uri = 'mongodb://'+user+':'+pwd+"@"+server+':'+port +'/' + dbname
    client = pymongo.MongoClient(uri)
    # 指向数据库
    mdb = client['dbylqx']
    # 获取集合名
    collec_ylqx = mdb['collec_ylqx']
    return collec_ylqx


if __name__ == '__main__':
    collec_ylqx = get_collection()
    get_cate()





