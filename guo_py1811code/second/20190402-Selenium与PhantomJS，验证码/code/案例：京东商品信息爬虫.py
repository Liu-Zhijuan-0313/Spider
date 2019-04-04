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

url = 'https://www.jd.com/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(1)
# 搜索关键字的输入框
tb_input = driver.find_element_by_css_selector('#key')
# 搜索按钮
search_btn = driver.find_element_by_css_selector('.button')

tb_input.clear()
tb_input.send_keys('手机')
time.sleep(2)
search_btn.click()

time.sleep(random.random()*2)

# 模拟下拉滚动条到底部
for i in range(0,5):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(random.random()*2)

# 商品信息的提取
good_ls = driver.find_elements_by_css_selector('.gl-item')
print('good len:',len(good_ls))

for info in good_ls:
    title = info.find_element_by_css_selector('.p-name.p-name-type-2 > a').text.strip()
    price = info.find_element_by_css_selector('.p-price').text.strip()
    print('title:',title)
    print('price:',price)
    print('='*60)

driver.close()



