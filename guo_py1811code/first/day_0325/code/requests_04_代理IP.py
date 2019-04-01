import requests

# 根据协议类型，选择不同的代理116.209.52.25	9999
proxies = {
  #"http": "http://101.236.21.22:8866",
  "http": "http://116.209.52.25:9999",
}

response = requests.get("http://www.baidu.com", proxies = proxies)
print(response.content.decode('utf-8'))