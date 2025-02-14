from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about.html", views.index, name="index"),
    path("service.html", views.index, name="index"),
    path("team.html", views.index, name="index"),
    path('login', views.processlogin, name="login"),
    path('logout', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]