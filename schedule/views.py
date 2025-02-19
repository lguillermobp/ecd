from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from dispatchplan.models import *
from datetime import datetime
import json

# Create your views here.
def index(request, plid):
    
    ctx={"nametittle":"LPR"}
    return render(request, 'schedule_index.html', ctx)