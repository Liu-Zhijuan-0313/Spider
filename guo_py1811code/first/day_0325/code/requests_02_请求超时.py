import requests

try:
    heders = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(' http://www.baidu.com/', timeout=0.1)
    print(response.status_code)
except Exception as e:
    print(e)

