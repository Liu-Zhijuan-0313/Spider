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

headers = {
    'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
    'Cookie':'SINAGLOBAL=5939010367539.148.1549091749763; UOR=news.ifeng.com,widget.weibo.com,www.51testing.com; login_sid_t=4c35d76930c4f3e6584b49471ddb76c8; cross_origin_proto=SSL; Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; YF-V5-G0=2583080cfb7221db1341f7a137b6762e; WBStorage=201903260940|undefined; wb_view_log=1920*10801; _s_tentry=-; Apache=8121133499040.986.1553564416994; ULV=1553564417015:17:5:1:8121133499040.986.1553564416994:1553263682310; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5i18Aw7NyeAg6CaaNECPyx5JpX5K2hUgL.Foqceh50Sh27eK52dJLoIEXLxK-LBK-L1hMLxK-LBo5L12qLxK.L1h-LBoMLxK-LB.-LB--LxK-L12BL1-2t; SSOLoginState=1553564441; ALF=1585100457; SCF=Auu3vxzdMjAXakGjpu9r_b7dhpijavMuX8MAoUCKws1PSADVvCW8sZsFEzgAAAud7-aq0kL2na0GkXD06UevHAU.; SUB=_2A25xnfN6DeRhGeBI61IS9C_MyjyIHXVS62OyrDV8PUNbmtBeLRSikW9NRqLCtxz2SvikuqP9Z2TIawuxyuNM_KVM; SUHB=0N21R1Lwl1-sUj; un=3414018462@qq.com; wvr=6; wb_view_log_6600341010=1920*10801; YF-Page-G0=70333fc8bc96e3a01b1d703feab3b41c|1553564465|1553564465; webim_unReadCount=%7B%22time%22%3A1553564474894%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D'
           }

response = requests.get('https://weibo.com/u/6600341010/home?wvr=5&lf=reg',headers=headers)
print(response.text)
print(response.status_code)
