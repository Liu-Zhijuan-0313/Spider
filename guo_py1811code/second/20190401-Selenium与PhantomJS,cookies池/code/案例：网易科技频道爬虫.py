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

from selenium import webdriver
import time
import random

# 页面请求
browser = webdriver.Chrome()
browser.get('http://tech.163.com/')
last_height = browser.execute_script("return document.body.scrollHeight;")
while True:
    print('页面加载....')
    # 滑动条拖动一次
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    # 加载等待
    time.sleep(random.random()*10)
    # 计算一个新的高度
    new_height = browser.execute_script("return document.body.scrollHeight;")
    print(last_height, new_height)
    if new_height == last_height:
        break;
    last_height = new_height

# html = browser.page_source


# 数据提取
ls = browser.find_elements_by_css_selector('div.data_row.news_article.clearfix')
print('len:', len(ls))

for item in ls:
    title = item.find_element_by_css_selector('h3 > a').text
    print('title:',title)
    news_url = item.find_element_by_css_selector('h3 > a').get_attribute('href')
    print('new_url:',news_url)
    print('='*60)


browser.close()