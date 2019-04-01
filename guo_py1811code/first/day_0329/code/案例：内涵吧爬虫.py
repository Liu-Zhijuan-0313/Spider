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

def crawlDuanzi(pageNums):
    '''
    内涵吧的爬取
    :param pageNums:
    :return:
    '''
    curPage = 1
    while curPage <= pageNums:
        # 网页爬取
        if curPage == 1:
            url = 'https://www.neihan-8.com/article/index.html'
        else:
            url = 'https://www.neihan-8.com/article/index_'+str(curPage)+'.html'

        headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
        respose = requests.get(url,headers=headers)
        html = respose.content.decode()
        #print(html)
        # 数据提取
        pat_item = re.compile(r'<div class="text-column-item box box-790">(.*?<div class="view".*?>.*?</div>)',re.M | re.S)
        ls = pat_item.findall(html)
        print(len(ls))
        pat_title = re.compile(r'<h3>.*?<a.*?>(.*?)</a>',re.M | re.S)
        pat_url = re.compile(r'<h3>.*?<a.*?href="(.*?)"',re.M | re.S)
        pat_support = re.compile(r'<div.*?class="good".*?>(.*?)</div>', re.M | re.S)
        pat_against = re.compile(r'<div.*?class="bad".*?>(.*?)</div>', re.M | re.S)
        pat_views = re.compile(r'<div.*?class="view".*?>(.*?)</div>', re.M | re.S)
        pat_desc = re.compile(r'<div.*?class="desc".*?>(.*?)</div>', re.M | re.S)
        #pat_title = re.compile(r'', re.M | re.S)
        base_url = 'https://www.neihan-8.com/'
        for item in ls:
            #print(item)
            title = pat_title.search(item).group(1).strip()
            print('title:',title)
            url = base_url + pat_url.search(item).group(1).strip()
            print('url:', url)
            suport_nums =  pat_support.search(item).group(1).strip()
            print('suport_nums:', suport_nums)
            against_nums = pat_against.search(item).group(1).strip()
            print('against_nums:', against_nums)
            views_nums = pat_views.search(item).group(1).strip()
            print('views_nums:', views_nums)
            desc = pat_desc.search(item).group(1).strip()
            print('desc:', desc)

            print('='*60)

        # 数据存储

        curPage +=1


if __name__ == "__main__":
    nums = int(input('请输入爬取的页数：'))
    crawlDuanzi(nums)


