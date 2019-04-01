# 获取一个有登录信息的Cookie模拟登陆
from urllib import request
import chardet

# 1. 构建一个已经登录过的用户的headers信息
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#     # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，这个Cookie里记录了用户名，密码(通常经过RAS加密)
#     "Cookie": "SINAGLOBAL=3302089224669.22.1472035369223; un=3414018462@qq.com; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5i18Aw7NyeAg6CaaNECPyx5JpX5KMhUgL.Foqceh50Sh27eK52dJLoIEXLxK-LBK-L1hMLxK-LBo5L12qLxK.L1h-LBoMLxK-LB.-LB--LxK-L12BL1-2t; UOR=www.yiihuu.com,widget.weibo.com,tech.ifeng.com; SCF=AvEvZ-N1Nn2fjE8sghEjOeRpXyJf2tw7T2O4uTOBuLqdwp2NTu-RwgJlc3DZATipWSG0BlFhr_HfLvXiU-xQ6qI.; SUB=_2A25xMv3xDeRhGeBI61IS9C_MyjyIHXVSRmg5rDV8PUNbmtAKLXXMkW9NRqLCt0eHzIjyobXLkbdJGMeS5TacNvUP; SUHB=0mxU0epBmcmRH1; ALF=1578615072; SSOLoginState=1547079073; Ugrow-G0=169004153682ef91866609488943c77f; YF-V5-G0=a2489c19ecf98bbe86a7bf6f0edcb071; YF-Page-G0=0dccd34751f5184c59dfe559c12ac40a; wb_view_log_6600341010=1920*10801; _s_tentry=-; Apache=7550862659276.177.1547079126724; ULV=1547079126748:152:3:2:7550862659276.177.1547079126724:1546872819981",
# }

# # 2. 通过headers里的报头信息（主要是Cookie信息），构建Request对象https://www.baidu.com/
# req = request.Request("https://weibo.com/u/6600341010/home?wvr=5&lf=reg", headers = headers)
#
# # 3. 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），判断这是一个已经登录的用户，并返回相应的页面
# response = request.urlopen(req)
# # 4. 打印响应内容
# html = response.read()
# charset = chardet.detect(html)['encoding']
# print(charset)
# #print(html.decode(charset,'ignore'))

import requests
# 1. 构建一个已经登录过的用户的headers信息
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，这个Cookie里记录了用户名，密码(通常经过RAS加密)
    "Cookie": "anonymid=jru48ifmt3j3si; _r01_=1; ln_uact=17752558702; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; _de=32B20555AD3784A6BF2D3D01B72FE013; jebe_key=757177d7-4364-40db-be6b-cdd5b17c1d81%7C077a3e2b1c00096d5c13732ceee74ce5%7C1549513361097%7C1%7C1551858470234; depovince=GW; jebecookies=a63ced8a-74ea-4f0f-8a3d-8081b5b5867e|||||; JSESSIONID=abcBw69BBdAWu92C1eQMw; ick_login=35cfae73-b0cc-4c81-8fcc-a9f8ccb8e3aa; Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1553336590; Hm_lpvt_bfc6c23974fbad0bbfed25f88a973fb0=1553336620; p=78a2864fb08cd420e9d7735422c314ca2; first_login_flag=1; t=ac4860a9caa4ff859b2470a628f053312; societyguester=ac4860a9caa4ff859b2470a628f053312; id=966924492; xnsid=55ec2702; ver=7.0; loginfrom=null; jebe_key=757177d7-4364-40db-be6b-cdd5b17c1d81%7C077a3e2b1c00096d5c13732ceee74ce5%7C1553336624497%7C1%7C1553336624822; wp_fold=0",
}
response = requests.get('http://www.renren.com/966924492',headers=headers)
print(response.text)