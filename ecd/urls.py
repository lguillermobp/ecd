"""ecd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    path('', include("main.urls")),
    path('ppddashboard/', include("ppddashboard.urls")),
    path('netsuite/', include("netsuite.urls")),
    path('schedule/<plid>', include("schedule.urls")),
    path('lpr/', include("lpr.urls")),
    path('dispatchplan/<plid>/<csid>', include("dispatchplan.urls")),
    path('ppdprojections/<plid>/<csid>', include("ppdprojections.urls")),
    path("admin/", admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
