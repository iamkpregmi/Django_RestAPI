"""Company_Employee_API URL Configuration

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
# from rest_framework.authtoken import views
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CompanyAPI/',CompanyAPI.as_view()), # this is link for token based authentication
    path("company/",views.companies),
    path("company/<int:id>/",views.company),
    path("add_company/",views.add_company),
    path("edit_company/<int:id>/",views.edit_company),
    path("delete_company/<int:id>/",views.delete_company),
    # path('api-token-auth/', views.obtain_auth_token),
    path('register/',views.RegisterUser),

    path("employee/",views.employees),
    path("employee/<int:id>/",views.employee),
    path("add_employee/",views.add_employee),
    path("edit_employee/<int:id>/",views.edit_employee),
    path("delete_employee/<int:id>/",views.delete_employee),

    path("company/<int:id>/employee/",views.companyEmployee),#Custom URL
]

