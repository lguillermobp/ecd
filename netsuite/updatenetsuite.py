from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from models import *
from datetime import datetime
import json

def refreshing():
    listreg=Class_NetSuite()
    data= listreg.refreshdp()


refreshing()