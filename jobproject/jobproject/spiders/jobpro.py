import json
import re
import time
import scrapy
from jobproject.items import JobprojectItem

class JobproSpider(scrapy.Spider):
    name = 'jobpro'
    # allowed_domains = ['www.xxx.com']
    def __init__(self,name,*args,**kwargs):
        super(JobproSpider, self).__init__(*args,**kwargs)
        self.name = name
        self.page = 1
        #智能排序
        self.url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        self.start_urls = [self.url.format(self.name,self.page)]
        #最近排序
        # self.start_urls = [f'https://search.51job.com/list/000000,000000,0000,00,9,99,{self.name},2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=1&dibiaoid=0&line=&welfare=']
    #主函数
    def parse(self,response):
        # print(response.url)
        #获取职位总页数
        numbers = self.get_num(response)[0]
        # print(numbers)
        #遍历页数，构造url
        for number in range(1,int(numbers)+1):
            next_page_url = self.url.format(self.name,number)
            # print(next_page_url)
            #构造的Urlcallback到data_parse函数中
            yield scrapy.Request(url=next_page_url,callback=self.data_parse)
            print("-------------第%s页完成-------------" %number)
            time.sleep(1)
            # print(next_page_url)
            #设置页数
            if number == 4:
                break

    #解析函数
    def data_parse(self,response):
        # print(response.url)
        #获取json对象
        jsonObject = self.get_num(response)[1]
        for job_item in jsonObject["engine_search_result"]:
            items = JobprojectItem()
            items['job_name'] = job_item['job_name']
            items['company_name'] = job_item["company_name"]
            # 发布时间
            items['Releasetime'] = job_item['issuedate']
            items['salary'] = job_item['providesalary_text']
            items['site'] = job_item['workarea_text']
            try:
                # 如果attribute_text长度为4则包括工作经验，若为3则不包括工作经验
                if len(job_item['attribute_text']) == 3:
                    #学历要求
                    items['education'] = job_item['attribute_text'][1]
                    # 工作经验
                    items['Workexperience'] = ''
                else:
                    items['education'] = job_item['attribute_text'][2]
                    items['Workexperience'] = job_item['attribute_text'][1]
                # return  items
                print(items)
            except:
                pass
    #获取总页数,返回页数与json对象
    def get_num(self,response):
        # 定位数据位置，提取json数据
        search_pattern = "window.__SEARCH_RESULT__ = (.*?)</script>"
        jsonText = re.search(search_pattern, response.text, re.M | re.S).group(1)

        # 解析json数据
        jsonObject = json.loads(jsonText)
        number = jsonObject['total_page']
        return number,jsonObject

    # def dataparse(self, response):
    #     #定位数据位置，提取json数据
    #     search_pattern = "window.__SEARCH_RESULT__ = (.*?)</script>"
    #     jsonText = re.search(search_pattern, response.text, re.M | re.S).group(1)
    #
    #     #解析json数据
    #     jsonObject = json.loads(jsonText)
    #     for job_item in jsonObject["engine_search_result"]:
    #         items = JobprojectItem()
    #         items['job_name'] = job_item['job_name']
    #         items['company_name'] = job_item["company_name"]
    #         #发布时间
    #         items['Releasetime'] = job_item['issuedate']
    #         items['salary'] = job_item['providesalary_text']
    #         items['site'] = job_item['workarea_text']
    #         #如果attribute_text长度为4则包括工作经验，若为3则不包括工作经验
    #         if len(job_item['attribute_text']) == 3:
    #             items['education'] = job_item['attribute_text'][1]
    #             #工作经验
    #             items['Workexperience'] = ''
    #         else:
    #             items['education'] = job_item['attribute_text'][2]
    #             items['Workexperience'] = job_item['attribute_text'][1]
    #         # yield scrapy.Request()
    #         return  items

