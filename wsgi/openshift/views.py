import os
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def home(request):
    return render_to_response('home/home.html')

def dashboard(request):
    try:
        t = get_template('dashboard.html')
            html = t.render()
    except:
        print sys_exec_info()[0]
    return HttpResponse(html)
