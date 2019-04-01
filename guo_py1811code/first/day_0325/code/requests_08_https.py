import requests
import urllib3
urllib3.disable_warnings()
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',}
response = requests.get("https://www.12306.cn/mormhweb/",verify=False)



