# -*- coding: utf-8 -*-
import scrapy
from JobSpider.items import JobspiderItem
import re


class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition' # 爬虫的名字
    allowed_domains = ['51job.com'] # 限定爬取的域名
    start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']  # 列出了要爬取的url地址

    def __init__(self):
        self.city = 10000
        self.max_city = 40000
        self.page = 1
        self.max_page = 50
        self.str1 = 'https://search.51job.com/list/0'
        self.str2 = ',000000,0000,00,9,99,python,2,'
        self.str3 = '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='


    def get_url(self):
        return self.str1 + str(self.city) +self.str2 + str(self.page) + self.str3


    def parse(self, response):
        '''
        数据的解析提取
        :param response:
        :return:
        '''
        self.log('content:')
        #print('content:',response.body)
        job_list = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        print('len:',len(job_list))
        for each in job_list:
            name = each.xpath('./p/span/a/text()').extract()[0].strip()
            print('name:',name)
            corp = each.xpath('./span[@class="t2"]/a/text()').extract()[0].strip()
            print('corp:', corp)
            city = each.xpath('./span[@class="t3"]/text()').extract()[0].strip()
            print('city:', city)
            salary = each.xpath('./span[@class="t4"]/text()')
            if len(salary)>0:
                salary = salary.extract()[0].strip()
            else:
                salary = '空'
            print('salary:', salary)
            pub_date = each.xpath('./span[@class="t5"]/text()').extract()[0].strip()
            print('pub_date:', pub_date)
            print('='*60)

            # 封装item对象
            item = JobspiderItem()
            item['name'] = name
            item['corp'] = corp
            item['city'] = city
            item['salary'] = salary
            item['pub_date'] = pub_date

            # 将获取的数据提交给pipeline
            yield item

        # 从url中提取城市的编码
        p = self.str1 + r'(\d+).*'
        curcity = re.search(p,response.url).group(1)
        # 从url中提取当前页码
        p = self.str1 + curcity + self.str2 + r'(\d+).*'
        curpage = re.search(p,response.url).group(1)

        self.page = int(curpage) + 1
        print('curpage:',self.page)
        print('curcity:',curcity)

        if self.page <= self.max_page:
            url = self.get_url()
            # 封装请求对象，放入到请求等待队列
            yield scrapy.Request(url,callback=self.parse)
        else:
            self.city = int(curcity) + 10000
            self.page = 1
            url = self.get_url()
            print('city:',self.city)
            yield scrapy.Request(url,callback=self.parse)


