"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/14'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import re
pattern = re.compile(r'\d+')   # 查找数字

result1 = pattern.findall('hello 123456.789')
result2 = pattern.findall('one1two2three3four4', 0, 10)
result3 = pattern.findall('one1two2three3four4')
print(result1)
print(result2)
print(result3)




