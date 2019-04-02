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

loginname ='3414018462@qq.com'
password = 'qikuedu9527'


def login():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get('http://www.weibo.com/login.php')
        time.sleep(2)
        # 自动输入用户
        print('输入用户名....')
        driver.find_element_by_id('loginname').clear()  # 清除输入框中默认的内容
        driver.find_element_by_id('loginname').send_keys(loginname)
        time.sleep(2)
        # 自动输入密码
        print('输入密码....')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(password)
        time.sleep(2)
        # 点击登陆按钮
        driver.find_element_by_xpath('//div[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
        time.sleep(3)
        print(driver.current_url)
        print(driver.page_source)
        print('登陆成功.')
        time.sleep(10)
        driver.close()
    except Exception as e:
        print('登陆失败'+e)


if __name__ == '__main__':
    login()


