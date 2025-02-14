from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from dispatchplan.models import *
from datetime import datetime
import json

# Create your views here.


def index(request,plid,csid):
    listreg=DispatchPlan()
    updated_at = ""
    data= listreg.lista(plid,csid)
    datacust= listreg.listabycustomers(plid)

    if data:
        regupdated=data[0]
        updated_at=regupdated[9]
    ctx={"nametittle":"Insurance Company","regs":data,"updated":updated_at,"datacusts":datacust,"pldatas":listreg.pldata,"plid":plid,"csid":csid}
    return render(request, 'dp_index.html', ctx)

def dp_refreshnetsuite(request):
    print(request)
    listreg=Class_NetSuite()
    data= listreg.refreshdp()
    return redirect("/dispatchplan/all")