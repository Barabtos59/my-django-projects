"""
URL configuration for chilli project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showindex', views.showindex, name='showindex'),
    path('showlogin', views.showlogin, name='showlogin'),
    path('insertlogin', views.insertlogin, name='insertlogin'),
    path('insertfarmer_details', views.insertfarmer_details, name='insertfarmer_details'),
    path('showfarmerdetails', views.showfarmerdetails, name='showfarmerdetails'),
    path('insertownerdetails',views.insertownerdetails,name='insertownerdetails'),
    path('showownerdetails',views.showownerdetails,name='showownerdetails'),
    path('insertrate_chart', views.insertrate_chart, name='insertrate_chart'),
    path('showrate_chart', views.showrate_chart, name='showrate_chart'),
    path('insertrequest_for_storage', views.insertrequest_for_storage, name='insertrequest_for_storage'),
    path('showrequest_for_storage', views.showrequest_for_storage, name='showrequest_for_storage'),
    path('insertwarehouse_details', views.insertwarehouse_details, name='insertwarehouse_details'),
    path('showwarehouse_details', views.showwarehouse_details, name='showwarehouse_details'),
    path('showfarmerhome', views.showfarmerhome, name='showfarmerhome'),
    path('showownerhome', views.showownerhome, name='showownerhome'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('change_password', views.change_password, name='change_password'),
    path('logcheck', views.logcheck, name='logcheck'),


]
