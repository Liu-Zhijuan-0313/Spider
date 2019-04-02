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

# 导入 webdriver
from selenium import webdriver
import time

# 调用环境变量指定的Chrome浏览器创建浏览器对象
driver = webdriver.Chrome()
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
time.sleep(1)
driver.get("http://www.baidu.com/")
# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id("kw").send_keys("奇酷信息")
time.sleep(1)
# id="su"是百度搜索按钮，click() 是模拟点击
driver.find_element_by_id("su").click()
time.sleep(1)
# 获取新的页面快照
driver.save_screenshot("./images/奇酷信息.png")
time.sleep(1)
# 清除输入框内容
driver.find_element_by_id("kw").clear()
# 关闭当前页面，如果只有一个页面，会关闭浏览器
time.sleep(5)
driver.close()
# 关闭浏览器
driver.quit()
