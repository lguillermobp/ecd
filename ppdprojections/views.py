from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from ppdprojections.models import *
from datetime import datetime
import json

# Create your views here.
def index(request, plid,csid):
    
    ctx={"nametittle":"LPR"}
    return render(request, 'ppdprojections_index.html', ctx)