from django.contrib import admin
from .models import Company

class Company_Admin(admin.ModelAdmin):
    list_display= ("company_id", "name", "location", "type")
    search_fields = ("name",)
    list_filter = ("type",)
admin.site.register(Company,Company_Admin)