from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic.base import View
from .models import app51data
import json
# def index(request):
#     # return HttpResponse("hello world")
#     # return render(request,'index.html')
#     data =app51data.objects.all()
#     list3 = []
#     i = 1
#     for var in data:
#         data = {}
#         data['id'] = i
#         data['Releasetime'] = var.Releasetime
#         data['job_name'] = var.job_name
#         data['salary'] = var.salary
#         data['site'] = var.site
#         data['education'] = var.education
#         data['company_name'] = var.company_name
#         data['Workexperience'] = var.Workexperience
#         list3.append(data)
#         i += 1
#
#     # a = json.dumps(data)
#     # b = json.dumps(list2)
#
#     # 将集合或字典转换成json 对象
#     c = json.dumps(list3)
#     return HttpResponse(c)


class ReadView(View):
    def get(self,request):
        all_data = app51data.objects.all()
        return render(request,'index.html',{"all_data":all_data})