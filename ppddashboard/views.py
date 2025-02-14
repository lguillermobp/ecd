from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from ppddashboard.models import *
from datetime import datetime
import json

# Create your views here.


def index(request):
    listreg=PPD()
    data= listreg.lista()
    regupdated=data[0]
    updated_at=regupdated[18]
    ctx={"nametittle":"Insurance Company","regs":data,"updated":updated_at} 
    return render(request, 'ppd_index.html', ctx)

def ppd_refreshnetsuite(request):
    listreg=Class_NetSuite()
    data= listreg.refreshppd()
    return redirect("/ppddashboard")
    
