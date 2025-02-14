from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from main.models import *
from datetime import datetime
import json

# Create your views here.

def index(request):
    
    ctx={"nametittle":"Insurance Company","regs":"data"}
    return render(request, 'index.html', ctx)


def logout_view(request):

    logout(request)
    return redirect('login') # Replace 'login' with the name of your login page URL


def processlogin(request):

    if request.method == 'POST':
        iduser = request.POST['iduser']
        password = request.POST['password']
        user = auth.authenticate(username=iduser,password=password)

        if user is not None:
            auth.login(request, user)

            
            return redirect("/")

        else:
            desmsg="User or password no valid"
            messages.info(request, desmsg)
            print('Password no valid')
            return render(request, "index.html")
    else:

         # send_mail("Asunto", "mensaje", "lguillermobp@gmail.com", ["gabc13082002@gmail.com"])
        ctx={"nametittle":"Login"}
    
    return render(request, "login.html", ctx)