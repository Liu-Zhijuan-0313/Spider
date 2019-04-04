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

browser = webdriver.Chrome()
for page in range(1,10):
    url = 'http://www.dianping.com/shanghai/hotel/g3020p'+str(page)
    browser.get(url)
    # 数据提取
    ls = browser.find_elements_by_xpath('//ul[@class="hotelshop-list"]/li')
    print('page:',page,'len:',len(ls))
    for item in ls:
        title = item.find_element_by_xpath('.//a[@class="hotel-name-link"]').text
        print('title:',title)
        place = item.find_element_by_xpath('.//p[@class="place"]').text
        print('place:',place)
        price = item.find_element_by_xpath('.//div[@class="price"]//strong').text
        print('price:',price)
        print('='*60)
    time.sleep(random.random()*2)





