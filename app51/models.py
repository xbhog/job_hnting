from django.db import models

# Create your models here.
#定义app51的数据模型
class app51data(models.Model):
    #发布时间,长度20
    Releasetime = models.CharField(max_length=20)
    #职位名，长度50
    job_name =models.CharField(max_length=50)
    #薪水
    salary = models.CharField(max_length=20)
    #工作地点
    site = models.CharField(max_length=50)
    #学历水平
    education = models.CharField(max_length=20)
    #公司名称
    company_name = models.CharField(max_length=50)
    #工作经验
    Workexperience = models.CharField(max_length=20)
