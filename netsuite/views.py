from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from netsuite.models import *
from datetime import datetime
import json


# Create your views here.
def dp_refreshnetsuite(request):
    print(request)
    listreg=Class_NetSuite()
    data= listreg.refreshdp()
    return redirect("/dispatchplan/all/all")