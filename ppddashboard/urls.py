from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("", login_required(views.index), name="index"),
    path("ppd_refreshnetsuite", login_required(views.ppd_refreshnetsuite), name="ppd_refreshnetsuite")
]