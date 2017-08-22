# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request,'hello.html', context)    #render提交表单