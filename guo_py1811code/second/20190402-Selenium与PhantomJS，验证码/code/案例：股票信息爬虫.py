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
import json
import pymysql
import re
import math

count_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?'
data_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?'

type_list = ['sh_a', 'sh_b', 'sz_a', 'sz_b', 'sh_z', 'sz_z']
page = 1
size = 40
pat1 = re.compile(r'"(\d+)"')
pat2 = re.compile(r'\{(.*?)\}')
headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

for type in type_list:
    params1 = {
        'node': type
    }
    html = requests.get(url=count_url, params=params1, headers=headers).text
    count = int(pat1.search(html).group(1))
    page_count = math.ceil(count / size)
    print(count, page_count)
    for page in range(1, page_count + 1):
        params2 = {
            'page': page,
            'num': 40,
            'sort': 'symbol',
            'asc': '1',
            'node': type,
            '_s_r_a': ' init'
        }
        print('type:',type,'page:',page)
        html = requests.get(data_url,params=params2,headers=headers).text
        #print(html)
        ls = pat2.findall(html)
        for item in ls:
            print(item)
            tmps = item.split(',')
            for temp in tmps:
                tmps2 = temp.split(':')
                print(tmps2[0],'=====',tmps2[1])

        print("="*60)


