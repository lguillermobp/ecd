from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("dp_refreshnetsuite", login_required(views.dp_refreshnetsuite), name="dp_refreshnetsuite")
]