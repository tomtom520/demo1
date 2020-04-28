"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from booktest import views

urlpatterns = [
    url('^static_test$', views.static_test, name='static_test'),
    url('^index$', views.index, name='index'),
    url(r'^upload_handle$', views.upload_handle, name='upload_handle'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^show_area(?P<pindex>\d*)$', views.show_area, name='show_area'), # 先分组，在用？P取组名，再用\d*  匹配数字  可以有可以没有
    url(r'^areas$', views.areas, name='areas'),
    url(r'^prov$', views.prov, name='prov'),
    url(r'^city(\d+)$', views.city, name='city'),
    url(r'^xian(\d+)$', views.city),
]
