import requests
response = requests.get("http://www.baidu.com/")
print(type(response))
print(response.text)
# 也可以这么写
# response = requests.request("get", "http://www.baidu.com/")
# 查看响应内容，response.content返回的字节流数据
print(response.content)
print(response.content.decode('utf8'))
# 查看响应内容，response.text 返回的是Unicode格式的数据
print(response.text)
# 查看完整url地址
print(response.url)
# 查看响应头部字符编码
print(response.encoding)
# 查看响应码
print(response.status_code)
# 查看响应头
print(response.headers)
# 查看请求头
print(response.request.headers)

# 'User-Agent': 'python-requests/2.21.0'
