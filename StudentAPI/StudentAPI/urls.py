"""StudentAPI URL Configuration

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
from mainApp import views
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',views.students),
    path('students/<id>',views.single_student),
    path('add_student/',views.add_student),
    path('edit_student/<id>',views.edit_student),
    path('delete_student/<id>',views.delete_student),
    path('get_book/',views.get_book),
    path('studentapi/',StudentAPI.as_view()), # this is the API view link for all Operations
]
