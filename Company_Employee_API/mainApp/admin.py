from django.contrib import admin
from .models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','company_name','city','company_type')

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('id','name','department','salary',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department', 'salary', 'get_company_name')

    def get_company_name(self, obj):
        return obj.Company_Name.company_name  # Access the related Company's name

    get_company_name.short_description = 'Company Name'  # Set the column header in admin panel


admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)

