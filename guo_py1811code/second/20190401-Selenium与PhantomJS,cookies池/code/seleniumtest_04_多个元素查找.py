"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/24'
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
from selenium import webdriver

# 获取商品分类
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
lis = browser.find_elements_by_css_selector('.service-bd li')
print(len(lis))
li_list = browser.find_elements_by_tag_name('li')
print(len(li_list))
class_list = browser.find_elements_by_class_name('service-bd')
print(len(class_list))
xpath_list = browser.find_elements_by_xpath('//div[@class="service J_Service"]')
print(len(xpath_list))
linktext_list = browser.find_elements_by_link_text('美妆')
print(len(linktext_list))
browser.close()


