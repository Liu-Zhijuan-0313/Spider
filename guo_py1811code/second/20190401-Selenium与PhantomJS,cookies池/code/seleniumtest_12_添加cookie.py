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

driver = webdriver.Chrome()
# driver.get("http://member.rltxtest.xyz/login/login.html")
driver.get ("http://www.youdao.com")
# 向cookie中name和value中添加回话信息,
driver.add_cookie({'name': 'key-aaaaaaa','value': 'value-bbbbb'})
# 遍历cookie中name和value信息并打印对应的信息，并包括添加对应的信息
for cookie in driver.get_cookies():
    print("%s->%s" % (cookie['name'], cookie['value']))
driver.quit ()

