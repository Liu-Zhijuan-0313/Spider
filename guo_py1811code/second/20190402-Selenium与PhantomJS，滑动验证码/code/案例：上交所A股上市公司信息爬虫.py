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

url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback17900&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=1&_=1554196431045'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Cookie':'yfx_c_g_u_id_10000042=_ck19022622490319840335861103860; VISITED_MENU=%5B%228528%22%5D; sseMenuSpecial=8527; yfx_f_l_v_t_10000042=f_t_1551192543942__r_t_1554196238137__v_t_1554196238137__r_c_2',
    'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'
}

response = requests.get(url,headers=headers)
print(response.text)
print(response.status_code)