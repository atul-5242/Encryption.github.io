"""Forpractices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Forpractices import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.userform),
    # path('new/', views.new),
    # path('Worng_pass/', views.w_pass),
    # path('www.google.com', views.Google),
    # path('submitform/', views.submitform,name="submitform"),
    path('saveform/', views.saveform,name="saveform"),
    path('savedata/', views.savedata,name="savedata"),
    
]
