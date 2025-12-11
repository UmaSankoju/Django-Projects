"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from basic.views import base, home, about, services, contactus, sample, sample1, studentdata, productinfo, pagination

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='base'),
    path('home/', home, name='home'),  # <-- add name here
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contactus, name='contact'),
    path('sample/', sample),
    path('sample1/', sample1),
    path('studentdata/', studentdata),
    path('productinfo/', productinfo),
    path('pagination/',pagination)
]

